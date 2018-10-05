from gtts import gTTS
import os,time
import io

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types


path_to_watch = "/home/gunnika/Pictures/Webcam"

before = dict ([(f, None) for f in os.listdir (path_to_watch)])

# IMAGE TO TEXT FUNCTION

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
       #   text_file.write(a)


while (1):
  time.sleep (1)
  after = dict ([(f, None) for f in os.listdir (path_to_watch)])

  added = [f for f in after if not f in before]
  removed = [f for f in before if not f in after]

  if (added): 
    print ("Added: ", ", ".join (added))
    new_path = '/home/gunnika/Pictures/Webcam/'+added[0]
    detect_text(new_path)

  if (removed): 
  	print ("Removed: ", ", ".join (removed))
  before = after

# Instantiates a client


