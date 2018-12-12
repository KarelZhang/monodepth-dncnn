import cv2
import numpy as np
def generateBmp(filename,holder):
    print(filename)
    lenna = cv2.imread(filename)
    row, col, channel = lenna.shape
    lenna_gray = np.zeros((row, col))
    for r in range(row):
        for l in range(col):
            lenna_gray[r, l] = 1 / 3 * lenna[r, l, 0] + 1 / 3 * lenna[r, l, 1] + 1 / 3 * lenna[r, l, 2]

    cv2.imwrite(filename.split('/')[-1]+holder+".bmp", lenna_gray.astype("uint8"))

def readandgenerate(filename,num=5):
    with open(filename,"r") as f:
        for i in range(num):
            line =f.readline()
            path1= line.split(" ")[0]
            path2 =line.split(" ")[1].replace("\n","")
            basepath ="/media/zhangjiaao/data/kitti/"
            generateBmp(basepath+path1,holder="L")
            generateBmp(basepath + path2,holder="R")
readandgenerate("new_test_files.txt")
