import pytesseract
import PIL.Image
import cv2

myconfig = r"--psm 6 --oem 3 -l mon+eng"
img = cv2.imread("./uploadimages/testImage.png")
height,width , _ = img.shape

boxes = pytesseract.image_to_boxes(img, config = myconfig)

text = pytesseract.image_to_string(PIL.Image.open("./uploadimages/testImage.png"),config = myconfig)
for box in boxes.splitlines():
    box = box.split(" ")
    img = cv2.rectangle(img,(int(box[1]), height - int (box[2])), (int(box[3]) ,height- int (box[4] )), (0,255,0), 1)

cv2.imshow("Result:",img)
cv2.waitKey(0)
print (text)


