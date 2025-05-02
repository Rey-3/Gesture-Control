from video_stream import VideoStream
from hand_tracker import HandTracker
from mouse_controller import MouseController
from click_detector import ClickDetector
from double_click_detector import DoubleClickDetector
from right_click_detector import RightClickDetector
import cv2
import pyautogui
import time
import os
import datetime
#---------------------------------------------------------------------------
# 20/04/2025 updated by Zhi Yang (added double click detection)
# 2/05/2025 updated by Hong Seng (added right click detection)
# 2/05/2025 updated by Hong Seng (added gesture logging functionality)
#---------------------------------------------------------------------------


# Constants
ALPHA = 0.5
MOVE_THRESHOLD = 2
LOG_FOLDER = "logs"  # Folder to store log files

def create_log_file():
    # Create a log file with current timestamp and return file handler.
    if not os.path.exists(LOG_FOLDER):
        os.makedirs(LOG_FOLDER)
    
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_file_path = os.path.join(LOG_FOLDER, f"gesture_log_{timestamp}.txt")
    
    # Create and initialize log file
    with open(log_file_path, "w") as log_file:
        log_file.write(f"=== Gesture Control Log Started at {timestamp} ===\n")
        log_file.write("Timestamp, Gesture, Action\n")
    
    print(f"Log file created at: {log_file_path}")
    return log_file_path

def log_gesture(log_file_path, gesture, action):
    # Log the detected gesture and action to the log file.
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
    log_entry = f"{timestamp}, {gesture}, {action}\n"
    
    with open(log_file_path, "a") as log_file:
        log_file.write(log_entry)

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
    # Capture frames, track hand, move mouse, detect clicks, and display.
    screen_width, screen_height = pyautogui.size()
    
    # Create a log file for this session
    log_file_path = create_log_file()

    vs = VideoStream(src=0)
    hand_tracker = HandTracker()
    mouse_controller = MouseController(alpha=ALPHA, threshold=MOVE_THRESHOLD)
    click_detector = ClickDetector()
    double_click_detector = DoubleClickDetector()
    right_click_detector = RightClickDetector()
    
    # Track the last known states to avoid redundant logging
    last_moving = False
    last_click = False
    last_double_click = False
    last_right_click = False

    try:
        while True:
            frame = vs.read()
            if frame is None:
                continue

            frame = cv2.flip(frame, 1)
            hand_landmarks = hand_tracker.detect(frame)

            # Draw landmarks on the frame
            hand_tracker.draw_landmarks(frame, hand_landmarks)

            # Log gesture detection and actions
            current_moving = False
            current_click = False
            current_double_click = False 
            current_right_click = False

            if hand_landmarks and is_move_gesture(hand_landmarks):
                current_moving = True
                
                # Compute target mouse position
                index_tip = hand_landmarks.landmark[8]
                target_x = int(index_tip.x * screen_width)
                target_y = int(index_tip.y * screen_height)

                # Smooth mouse movement
                mouse_controller.update(target_x, target_y)
                
                # Log mouse movement only when it first starts
                if not last_moving:
                    log_gesture(log_file_path, "Move", f"Mouse moved to {target_x},{target_y}")

                # Detect and perform click if gesture is present
                if click_detector.should_click(hand_landmarks):
                    current_click = True
                    if not last_click:
                        click_detector.detect_and_click(hand_landmarks)
                        log_gesture(log_file_path, "Click", "Left mouse click")
                else:
                    click_detector.click_in_progress = False
                
                # Detect and perform double-click if gesture is present
                if double_click_detector.should_double_click(hand_landmarks):
                    current_double_click = True
                    if not last_double_click:
                        double_click_detector.detect_and_double_click(hand_landmarks)
                        log_gesture(log_file_path, "Double Click", "Mouse double click")
                else:
                    double_click_detector.double_click_in_progress = False
                
                # Detect and perform right-click if gesture is present
                if right_click_detector.should_right_click(hand_landmarks):
                    current_right_click = True
                    if not last_right_click:
                        right_click_detector.detect_and_right_click(hand_landmarks)
                        log_gesture(log_file_path, "Right Click", "Right mouse click")
                else:
                    right_click_detector.right_click_in_progress = False

            # Update last known states
            last_moving = current_moving
            last_click = current_click
            last_double_click = current_double_click
            last_right_click = current_right_click

            # Show the video feed
            cv2.imshow('Optimized Control (Esc to Exit)', frame)

            # Exit on ESC key
            if cv2.waitKey(1) & 0xFF == 27:
                log_gesture(log_file_path, "Exit", "Program terminated by user")
                break
            
    except Exception as e:
        error_msg = f"An error occurred: {e}"
        print(error_msg)
        log_gesture(log_file_path, "Error", error_msg)

    finally:
        # Clean up resources
        vs.stop()
        cv2.destroyAllWindows()
        log_gesture(log_file_path, "Shutdown", "Program stopped")

def main():
    # Entry point.
    run_control_loop()

if __name__ == '__main__':
    main()
