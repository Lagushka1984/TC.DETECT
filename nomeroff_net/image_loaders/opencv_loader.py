import os
import cv2
from .base import BaseImageLoader


class OpencvImageLoader(BaseImageLoader):
    link: str = "rtsp://"
    tty: int = 0

    def __init__(self):
        self.cap = cv2.VideoCapture(self.tty)

    def load_from_cap(self):
        _, img = self.cap.read()
        img = img[..., ::-1]
        return img

    @staticmethod
    def load_from_file(img_path):
        img = cv2.imread(img_path)
        img = img[..., ::-1]
        return img


if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    img_file = os.path.join(current_dir, "../../data/examples/oneline_images/example1.jpeg")

    image_loader = OpencvImageLoader()
    loaded_img = image_loader.load_from_file(img_file)
