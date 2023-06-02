import cv2

if __name__ == '__main__':
    img_path = './10_git_github/assets/2023-05-26 143634.png'
    img = cv2.imread(img_path)
    cv2.imshow('test', img)
    cv2.waitKey(0)
