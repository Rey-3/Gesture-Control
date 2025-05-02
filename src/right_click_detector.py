import math
import pyautogui

# ---------------------------------------------------------------------
# Name: RightClickDetector
# Author: Hong Seng
# Description:
# A class to detect a "right-click" gesture using the ring finger joints
# based on the angles between landmarks. If the gesture is detected,
# it simulates a mouse right-click using pyautogui. Designed to avoid 
# repeated right-clicks by requiring the hand to return to a "non-right-click" pose
# before allowing the next right-click.
# -----------------------------------------------------------------------
class RightClickDetector:
    def __init__(self, angle_threshold_deg=170):
        # Convert the angle threshold from degrees to radians for calculation.
        # Default is 170°, assuming a straight finger is near 180°.
        self.angle_threshold = math.radians(angle_threshold_deg)
        
        # Flag to prevent continuous right-clicking; reset only when gesture is released.
        self.right_click_in_progress = False

    def compute_angle(self, a, b, c):
        # Calculates the angle formed at point 'b' using three (x, y) coordinates.
        BA = (a[0] - b[0], a[1] - b[1])
        BC = (c[0] - b[0], c[1] - b[1])
        dot_product = BA[0]*BC[0] + BA[1]*BC[1]
        norm_BA = math.hypot(*BA)
        norm_BC = math.hypot(*BC)

        if norm_BA == 0 or norm_BC == 0:
            return 0
        angle = math.acos(dot_product / (norm_BA * norm_BC))
        return angle

    def should_right_click(self, landmarks) -> bool:
        """
        Determines whether a right-click gesture is made based on the ring finger angles.
        Uses the ring finger (finger #3) for the right-click gesture.
        
        Checks two angles:
        - Angle at joint 14: between points 13-14-15
        - Angle at joint 15: between points 14-15-16

        If both angles are less than the threshold, the finger is considered bent (right-click gesture).
        """
        # Ring finger points
        p13 = (landmarks.landmark[13].x, landmarks.landmark[13].y)
        p14 = (landmarks.landmark[14].x, landmarks.landmark[14].y)
        p15 = (landmarks.landmark[15].x, landmarks.landmark[15].y)
        p16 = (landmarks.landmark[16].x, landmarks.landmark[16].y)

        # Check if ring finger is bent
        angle1 = self.compute_angle(p13, p14, p15)
        angle2 = self.compute_angle(p14, p15, p16)

        # Ring finger needs to be bent for right-click
        return angle1 < self.angle_threshold and angle2 < self.angle_threshold

    def detect_and_right_click(self, landmarks):
        # Triggers a mouse right-click if the right-click gesture is detected and not already in progress.
        # Resets the right-click flag when the gesture is no longer detected.
        if self.should_right_click(landmarks):
            if not self.right_click_in_progress:
                pyautogui.rightClick()  # Simulate mouse right-click
                self.right_click_in_progress = True
        else:
            self.right_click_in_progress = False 