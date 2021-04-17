import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
img = cv2.imread('assets/test_image2.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

hImg, wImg, _ = img.shape
boxes = pytesseract.image_to_boxes(img)

for box in boxes.splitlines():
	box = box.split(' ')
	x, y, w, h = int(box[1]), int(box[2]), int(box[3]), int(box[4])
	cv2.rectangle(img, (x, hImg-y), (w, hImg-h), (0,0,255), 1)
	cv2.putText(img, box[0], (x, hImg-y+15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (50,50,255), 1, cv2.LINE_AA)

cv2.imshow('Result', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
