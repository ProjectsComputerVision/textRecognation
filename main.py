import cv2
import numpy as np
import matplotlib.pyplot as plt
import pytesseract
from PIL import Image


def get_string(img_path):
    # Read image with opencv
    img = cv2.imread(img_path)
    # Convert to gray
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # threshold to get just the signature (INVERTED)
    ret, threshed_img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
    # plt.imshow(threshed_img, cmap='gray')
    # plt.show()
    # text recognition
    data = pytesseract.image_to_string(threshed_img, lang='eng')
    # write text in a text file and save it to disk
    with open('output.txt', mode='w') as file:
        file.write(data)
    print(data)

img = get_string('kunuz.png')
# plt.imshow(img, cmap='gray')
# plt.show()