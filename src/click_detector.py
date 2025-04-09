import math
import pyautogui

# ---------------------------------------------------------------------
# Name: ClickDetector
#
# Description:
# A class to detect a "click" gesture using the index finger joints
# based on the angles between landmarks. If the gesture is detected,
# it simulates a mouse click using pyautogui. Designed to avoid 
# repeated clicks by requiring the hand to return to a "non-click" pose
# before allowing the next click.
# -----------------------------------------------------------------------
class ClickDetector:
    def __init__(self, angle_threshold_deg=170):
        # Convert the angle threshold from degrees to radians for calculation.
        # Default is 170°, assuming a straight finger is near 180°.
        self.angle_threshold = math.radians(angle_threshold_deg)
        
        # Flag to prevent continuous clicking; reset only when gesture is released.
        self.click_in_progress = False

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

    def should_click(self, landmarks) -> bool:
        """
        Determines whether a click gesture is made based on the index finger angles.
        Checks two angles:
        - Angle at joint 6: between points 5-6-7
        - Angle at joint 7: between points 6-7-8

        If both angles are less than the threshold, the finger is considered bent (click gesture).
        """
        p5 = (landmarks.landmark[5].x, landmarks.landmark[5].y)
        p6 = (landmarks.landmark[6].x, landmarks.landmark[6].y)
        p7 = (landmarks.landmark[7].x, landmarks.landmark[7].y)
        p8 = (landmarks.landmark[8].x, landmarks.landmark[8].y)

        angle1 = self.compute_angle(p5, p6, p7)
        angle2 = self.compute_angle(p6, p7, p8)

        return angle1 < self.angle_threshold and angle2 < self.angle_threshold

    def detect_and_click(self, landmarks):
        """
        Triggers a mouse click if the click gesture is detected and not already in progress.
        Resets the click flag when the gesture is no longer detected.
        """
        if self.should_click(landmarks):
            if not self.click_in_progress:
                pyautogui.click()  # 模拟鼠标左键点击
                self.click_in_progress = True
        else:
            self.click_in_progress = False
