import dlib
import cv2

# options = dlib.simple_object_detector_training_options()
# options.add_left_right_image_flips = True
# options.C = 2.3
#
# training_xml_path = '1_imglab.xml'
# output_model_path = 'ngu.svm'
#
# dlib.train_simple_object_detector(training_xml_path, output_model_path, options)
###---
detector = dlib.simple_object_detector("ngu.svm")

img = cv2.imread("./ziet/z5175103575216_3974484922df46450d8a12e56dbc3c4a.jpg")
dets = detector(img)

for det in dets:
    x, y, w, h = det.left(), det.top(), det.width(), det.height()
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow("Detected Objects", img)
cv2.waitKey(0)
cv2.destroyAllWindows()