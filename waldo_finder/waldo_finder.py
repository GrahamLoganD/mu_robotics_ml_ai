import cv2
import numpy

img_rgb = cv2.imread('waldo_finder/find_waldo.png', cv2.IMREAD_UNCHANGED)
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
template = cv2.imread('waldo_finder/waldo.png', cv2.IMREAD_GRAYSCALE)
h, w = template.shape

res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.6

loc = numpy.where(res >= threshold)
print(loc)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 2)
cv2.imwrite('found_waldo.png', img_rgb)
