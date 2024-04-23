import pytesseract
import PIL

myconfig = r"--psm 6 --oem 2 mon+eng "
text = pytesseract.image_to_string(PIL.Image.open("./uploadimages/2.jpg"), config=myconfig)
print(text)

