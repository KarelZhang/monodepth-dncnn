import numpy as np
import cv2

array = np.zeros((5, 256, 512), dtype=np.float32)
for i in range(5):
    image = cv2.imread("Image_0000000" + str(i + 1) + "_d.png", flags=cv2.IMREAD_GRAYSCALE)
    image = image / 8.0
    cv2.imshow("a"+str(i)+"",image)
    cv2.waitKey(1500)
    for j in image:
        print(j)
    image = cv2.resize(image, (512, 256))
    array[i] = image
cv2.waitKey(0)
np.save("test_traitional_5.npy", array)
