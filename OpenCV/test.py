import cv2
import numpy as np

if __name__ == '__main__':
    img_path = '/home/linxu/DataSpellProjects/MyJupyterWorkLab/lena.jpg'
    img_src = cv2.imread(img_path)
    cv2.imshow('src', img_src)
    cv2.waitKey()