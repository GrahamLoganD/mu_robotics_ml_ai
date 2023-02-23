import cv2
import numpy

COLOR_RED = (0, 0, 255)

image_rgb = cv2.imread(filename='waldo_finder/find_waldo.png',
                       flags=cv2.IMREAD_ANYCOLOR)
image_gray = cv2.cvtColor(src=image_rgb, code=cv2.COLOR_RGB2GRAY)
template = cv2.imread(filename='waldo_finder/waldo.png',
                      flags=cv2.IMREAD_GRAYSCALE)
template_height, template_width = template.shape

comparison = cv2.matchTemplate(image=image_gray, templ=template,
                               method=cv2.TM_CCOEFF_NORMED)
threshold = 0.6

locations = numpy.where(comparison >= threshold)
for top_left_point in zip(*locations[::-1]):
    top_left_point_x = top_left_point[0]
    top_left_point_y = top_left_point[1]
    bottom_right_point_x = top_left_point_x + template_width
    bottom_right_point_y = top_left_point_y + template_height
    bottom_right_point = (bottom_right_point_x, bottom_right_point_y)
    cv2.rectangle(img=image_rgb, pt1=top_left_point,
                  pt2=bottom_right_point, color=COLOR_RED, thickness=cv2.LINE_4)
cv2.imwrite(filename='found_waldo.png', img=image_rgb)
