import sys
import platform
import cv2
import pytesseract

if platform.system() == "Windows":
	pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
	print("You're on Windows")
else:
	print("You're probably on Linux")

img = cv2.imread(sys.argv[1])
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

hImg, wImg, _ = img.shape
boxes = pytesseract.image_to_boxes(img)
detected_text = pytesseract.image_to_string(img)

# Print the detected text to the console
print(detected_text)

for box in boxes.splitlines():
	box = box.split(' ')
	x, y, w, h = int(box[1]), int(box[2]), int(box[3]), int(box[4])
	# Show the detected text on the image alongwith bounding boxes
	cv2.rectangle(img, (x, hImg-y), (w, hImg-h), (0,0,255), 1)
	cv2.putText(img, box[0], (x, hImg-y+15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (50,50,255), 1, cv2.LINE_AA)

cv2.imshow('Result', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
