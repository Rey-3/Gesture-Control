import pyautogui

# --------------------------------------------------
# Name: MouseController
# Description:
# A class to control the mouse cursor smoothly by interpolating between
# the current position and the target position, using a weighted factor (alpha).
# The mouse moves when the distance from the previous position exceeds a threshold.
# --------------------------------------------------
class MouseController:
    # Initializes the MouseController with smoothing and movement threshold.
    # Parameters:
    #         alpha (float): A factor that controls the smoothness of the mouse movement.
    #                        A value closer to 1 makes the movement faster and less smooth.
    #                        Default is 0.5.
    #         threshold (int): The minimum distance the mouse needs to move before it is updated.
    #                          Default is 2 pixels.
    def __init__(self, alpha=0.5, threshold=2):
        self.alpha = alpha
        self.threshold = threshold
        self.prev_x, self.prev_y = pyautogui.position()

    
    # Updates the position of the mouse cursor based on the target position.
    # The movement is smoothed using the alpha factor, and movement is only performed
    # if the distance from the previous position exceeds the threshold.
    def update(self, target_x, target_y):
        current_x = int(self.prev_x + self.alpha * (target_x - self.prev_x))
        current_y = int(self.prev_y + self.alpha * (target_y - self.prev_y))

        if abs(current_x - self.prev_x) > self.threshold or abs(current_y - self.prev_y) > self.threshold:
            pyautogui.moveTo(current_x, current_y)
            self.prev_x, self.prev_y = current_x, current_y
