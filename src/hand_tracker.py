import cv2
import mediapipe as mp

# ----------------------------------------------------------------
# Name: HandTracker
# Description:
# A wrapper around MediaPipe's Hand Tracking module to detect and
# draw hand landmarks in a video frame. Useful for gesture-based
# interaction applications.
# -----------------------------------------------------------------
class HandTracker:
    # Initializes the MediaPipe hand detector with predefined parameters.
    def __init__(self):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            max_num_hands=1,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5,
            model_complexity=1
        )
        self.drawing = mp.solutions.drawing_utils

    # Detects hand landmarks in the given BGR frame.
    def detect(self, frame):
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(rgb_frame)
        return results.multi_hand_landmarks[0] if results.multi_hand_landmarks else None

    # Draws hand landmarks and connections on the provided frame.
    def draw_landmarks(self, frame, landmarks):
        self.drawing.draw_landmarks(
            frame, landmarks, self.mp_hands.HAND_CONNECTIONS,
            self.drawing.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=4),
            self.drawing.DrawingSpec(color=(255, 0, 0), thickness=2)
        )
