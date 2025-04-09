import cv2
import threading

# --------------------------------------------------------------
# Name: VideoStream
#
# Description:
# A threaded video stream class using OpenCV.
# Continuously captures frames from a video source (e.g., webcam)
# in a separate thread to improve performance and avoid frame lag.
# ----------------------------------------------------------------
class VideoStream:
    # Initializes the video capture object and starts the frame update thread
    def __init__(self, src=0, width=820, height=480):
        self.cap = cv2.VideoCapture(src)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
        self.ret, self.frame = self.cap.read()
        self.stopped = False
        self.lock = threading.Lock()
        threading.Thread(target=self.update, daemon=True).start()

    # Continuously captures frames from the video source in a separate thread.
    def update(self):
        while not self.stopped:
            ret, frame = self.cap.read()
            if not ret:
                self.stop()
                break
            with self.lock:
                self.frame = frame

    #Returns the most recent video frame in a thread-safe manner.
    def read(self):
        with self.lock:
            return self.frame.copy() if self.frame is not None else None

    # Stops the video stream and releases the video capture object
    def stop(self):
        self.stopped = True
        self.cap.release()
