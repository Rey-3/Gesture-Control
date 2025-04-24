from video_stream import VideoStream
from hand_tracker import HandTracker
from mouse_controller import MouseController
from click_detector import ClickDetector
from double_click_detector import DoubleClickDetector
import cv2
import pyautogui
import time
#---------------------------------------------------------------------------
# 20/04/2025 V0.3 updated by Zhi Yang (added double click detection)
# 21/04/2025 V0.4 updated by Zhi Yang (added operation logging to terminal)
#---------------------------------------------------------------------------


# Constants
ALPHA = 0.5
MOVE_THRESHOLD = 2

def is_move_gesture(landmarks):
    try:
        index_extended = landmarks.landmark[8].y < landmarks.landmark[6].y
        middle_folded = landmarks.landmark[12].y > landmarks.landmark[10].y
        ring_folded = landmarks.landmark[16].y > landmarks.landmark[14].y
        pinky_folded = landmarks.landmark[20].y > landmarks.landmark[18].y
        
        return index_extended and middle_folded and ring_folded and pinky_folded
    
    except (AttributeError, IndexError):
        return False

def run_control_loop():
    """Capture frames, track hand, move mouse, detect clicks, and display."""
    screen_width, screen_height = pyautogui.size()

    vs = VideoStream(src=0)
    hand_tracker = HandTracker()
    mouse_controller = MouseController(alpha=ALPHA, threshold=MOVE_THRESHOLD)
    click_detector = ClickDetector()
    double_click_detector = DoubleClickDetector()

    # For logging mouse movements (to avoid logging every tiny movement)
    last_logged_pos = None
    log_distance_threshold = 50  # Only log when moved this many pixels
    
    # Last state for detecting changes in actions
    last_click_in_progress = False
    last_double_click_in_progress = False

    print("Gesture control started. Press Esc to exit.")
    print("-----------------------------")
    print("Operation log:")

    try:
        while True:
            frame = vs.read()
            if frame is None:
                continue

            frame = cv2.flip(frame, 1)
            hand_landmarks = hand_tracker.detect(frame)

            # Draw landmarks on the frame
            hand_tracker.draw_landmarks(frame, hand_landmarks)

            if hand_landmarks and is_move_gesture(hand_landmarks):
                # Compute target mouse position
                index_tip = hand_landmarks.landmark[8]
                target_x = int(index_tip.x * screen_width)
                target_y = int(index_tip.y * screen_height)

                # Store previous position
                prev_x, prev_y = mouse_controller.prev_x, mouse_controller.prev_y
                
                # Smooth mouse movement
                mouse_controller.update(target_x, target_y)
                
                # Log significant mouse movements
                current_x, current_y = mouse_controller.prev_x, mouse_controller.prev_y
                if last_logged_pos is None:
                    last_logged_pos = (current_x, current_y)
                    print(f"[MOVE] Mouse moved to position: ({current_x}, {current_y})")
                elif (abs(current_x - last_logged_pos[0]) > log_distance_threshold or 
                      abs(current_y - last_logged_pos[1]) > log_distance_threshold):
                    print(f"[MOVE] Mouse moved to position: ({current_x}, {current_y})")
                    last_logged_pos = (current_x, current_y)

                # Detect and perform click if gesture is present
                click_detector.detect_and_click(hand_landmarks)
                
                # Log click actions
                if click_detector.click_in_progress and not last_click_in_progress:
                    print(f"[CLICK] At position ({current_x}, {current_y}) single click performed")
                last_click_in_progress = click_detector.click_in_progress
                
                # Detect and perform double-click if gesture is present
                double_click_detector.detect_and_double_click(hand_landmarks)
                
                # Log double-click actions
                if double_click_detector.double_click_in_progress and not last_double_click_in_progress:
                    print(f"[DOUBLE-CLICK] At position ({current_x}, {current_y}) double click performed")
                last_double_click_in_progress = double_click_detector.double_click_in_progress

            # Show the video feed
            cv2.imshow('Optimized Control (Esc to Exit)', frame)

            # Exit on ESC key
            if cv2.waitKey(1) & 0xFF == 27:
                print("Program exited")
                break
            
    except Exception as e:
      print(f"Error occurred: {e}")

    finally:
        # Clean up resources
        vs.stop()
        cv2.destroyAllWindows()

def main():
    """Entry point."""
    run_control_loop()

if __name__ == '__main__':
    main()
