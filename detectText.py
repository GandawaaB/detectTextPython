import pytesseract
import cv2
import PIL

myconfig = r"--psm 6 --oem 3 "
text = pytesseract.image_to_string(PIL.Image.open("./uploadimages/Capture.png"),  lang="mon+eng",config=myconfig)
print(text)

