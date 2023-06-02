import cv2
import argparse

parser = argparse.ArgumentParser(description='display an image')
parser.add_argument("-i", "--input_path", help="input image path", required=True, type=str)

if __name__ == '__main__':
    args = parser.parse_args()
    img_path = args.input_path
    # img_path = './10_git_github/assets/2023-05-26 143634.png'
    img = cv2.imread(img_path)
    cv2.imshow('test', img)
    cv2.waitKey(0)
