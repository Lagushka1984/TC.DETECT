import cv2
import numpy as np

class FrameType:
    def __init__(self) -> None:
        raise NotImplementedError("implement this method")

    def __call__(self) -> np.ndarray:
        raise NotImplementedError("implement this method")

class ImageType(FrameType):
    def __init__(self, path, name) -> None:
        self.name = name
        self.frame = cv2.imread(path)

    def __call__(self) -> np.ndarray:
        return self.frame

class VideoType(FrameType):
    def __init__(self, path, name) -> None:
        self.name = name
        self.cap = cv2.VideoCapture(path)

    def __call__(self) -> np.ndarray:
        _, rd = self.cap.read()
        return rd

class RTPSType(FrameType):
    def __init__(self, link, name) -> None:
        self.name = name
        self.link = link
        self.cap = cv2.VideoCapture(self.link)

    def __call__(self) -> np.ndarray:
        self.cap.open(self.link)
        _, rd = self.cap.read()
        self.cap.release()
        return rd