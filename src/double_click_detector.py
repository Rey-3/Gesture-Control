import math
import pyautogui

# ---------------------------------------------------------------------
# Name: DoubleClickDetector
# Author: Zhi Yang 
# Description:
# A class to detect a "double-click" gesture using both index and middle fingers
# based on the angles between landmarks. If the gesture is detected,
# it simulates a mouse double-click using pyautogui. Designed to avoid 
# repeated double-clicks by requiring the hand to return to a "non-double-click" pose
# before allowing the next double-click.
# -----------------------------------------------------------------------
class DoubleClickDetector:
    def __init__(self, angle_threshold_deg=170):
        # Convert the angle threshold from degrees to radians for calculation.
        # Default is 170°, assuming a straight finger is near 180°.
        self.angle_threshold = math.radians(angle_threshold_deg)
        
        # Flag to prevent continuous double-clicking; reset only when gesture is released.
        self.double_click_in_progress = False

    def compute_angle(self, a, b, c):
        """
        Calculates the angle formed at point 'b' using three (x, y) coordinates.
        """
        BA = (a[0] - b[0], a[1] - b[1])
        BC = (c[0] - b[0], c[1] - b[1])
        dot_product = BA[0]*BC[0] + BA[1]*BC[1]
        norm_BA = math.hypot(*BA)
        norm_BC = math.hypot(*BC)

        if norm_BA == 0 or norm_BC == 0:
            return 0
        angle = math.acos(dot_product / (norm_BA * norm_BC))
        return angle

    def should_double_click(self, landmarks) -> bool:
        """
        Determines whether a double-click gesture is made based on both index and middle fingers.
        The double-click gesture is defined as both index and middle fingers bent at the same time.
        
        Checks four angles:
        - Angles for index finger (joints 6 and 7)
        - Angles for middle finger (joints 10 and 11)
        
        If all four angles are less than the threshold, both fingers are considered bent (double-click gesture).
        """
        # Index finger points
        p5 = (landmarks.landmark[5].x, landmarks.landmark[5].y)
        p6 = (landmarks.landmark[6].x, landmarks.landmark[6].y)
        p7 = (landmarks.landmark[7].x, landmarks.landmark[7].y)
        p8 = (landmarks.landmark[8].x, landmarks.landmark[8].y)
        
        # Middle finger points
        p9 = (landmarks.landmark[9].x, landmarks.landmark[9].y)
        p10 = (landmarks.landmark[10].x, landmarks.landmark[10].y)
        p11 = (landmarks.landmark[11].x, landmarks.landmark[11].y)
        p12 = (landmarks.landmark[12].x, landmarks.landmark[12].y)

        # Check if index finger is bent
        index_angle1 = self.compute_angle(p5, p6, p7)
        index_angle2 = self.compute_angle(p6, p7, p8)
        
        # Check if middle finger is bent
        middle_angle1 = self.compute_angle(p9, p10, p11)
        middle_angle2 = self.compute_angle(p10, p11, p12)

        # Both index and middle fingers need to be bent for double-click
        return (index_angle1 < self.angle_threshold and 
                index_angle2 < self.angle_threshold and
                middle_angle1 < self.angle_threshold and 
                middle_angle2 < self.angle_threshold)

    def detect_and_double_click(self, landmarks):
        """
        Triggers a mouse double-click if the double-click gesture is detected and not already in progress.
        Resets the double-click flag when the gesture is no longer detected.
        """
        if self.should_double_click(landmarks):
            if not self.double_click_in_progress:
                pyautogui.doubleClick()  # Simulate mouse double-click
                self.double_click_in_progress = True
        else:
            self.double_click_in_progress = False

    