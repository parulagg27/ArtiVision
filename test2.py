from gtts import gTTS
import os
import io

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

# Instantiates a client
def detect_text(path):
    """Detects text in the file."""
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    #print('Texts:')
    for text in texts:
	    a=(('"{}"'.format(text.description)))
	    tts = gTTS(text=a, lang='en')
	    tts.save("abc.mp3")
	    os.system("mpg321 abc.mp3")
        #print(a)
        #with open("Output.txt", "w") as text_file:
       #     text_file.write(a)
    
    


if __name__ == "__main__":
	detect_text('file-page1.jpg')

