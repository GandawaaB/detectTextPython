from flask import Flask, request, jsonify
import werkzeug
import pytesseract
import PIL
app = Flask (__name__)  
@app.route('/upload', methods =["POST"] ) 
def upload():
    if(request.method=="POST"):
        imageFile = request.files['image']
        filename = werkzeug.utils.secure_filename(imageFile.filename)
        imageFile.save("./uploadimages/" + filename)
        conf = r"--psm 6 --oem 3"
        text = pytesseract.image_to_string(PIL.Image.open("./uploadimages/"+filename),config = conf,lang="eng" )
        print("text: ",text)
        return text

if(__name__) =='__main__':
    app.run(host="0.0.0.0") 