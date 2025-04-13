from video_stream import VideoStream
from hand_tracker import HandTracker
from mouse_controller import MouseController
from click_detector import ClickDetector
import cv2
import pyautogui
import time

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

                # Smooth mouse movement
                mouse_controller.update(target_x, target_y)

                # Detect and perform click if gesture is present
                click_detector.detect_and_click(hand_landmarks)

            # Show the video feed
            cv2.imshow('Optimized Control (Esc to Exit)', frame)


            # Exit on ESC key
            if cv2.waitKey(1) & 0xFF == 27:
                break
            
    except Exception as e:
      print(f"An error occurred: {e}")

    finally:
        # Clean up resources
        vs.stop()
        cv2.destroyAllWindows()

def main():
    """Entry point."""
    run_control_loop()

if __name__ == '__main__':
    main()
