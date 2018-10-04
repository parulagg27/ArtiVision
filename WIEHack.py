from flask import Flask
from gtts import gTTS
import requests
import os
app = Flask(__name__)

@app.route("/")
def home():
    return "<h1> Homepage </h1>"

@app.route('/audio',methods= ["POST","GET"])
def audio():
    tts = gTTS(text='Testing', lang='en')
    tts.save("test.mp3")
    #os.system("mpg321 test.mp3")
    return os.system('mpg321 test.mp3')

if __name__=='__main__':
    app.run(host='0.0.0.0',debug=True)