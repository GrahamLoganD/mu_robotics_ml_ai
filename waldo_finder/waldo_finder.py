import cv2
import numpy

img_rgb = cv2.imread('waldo_finder/find_waldo.png')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
template = cv2.imread('waldo_finder/waldo.png', 0)

w, h = template.shape[::-1] # What does this do?
