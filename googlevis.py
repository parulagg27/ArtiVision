import io
import os

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
    #for text in texts:
        #a=("{}".format(text.description))
    print('"{}"'.format(texts.description))
    


if __name__ == "__main__":
	detect_text('C:/Users/ANJALI/Anaconda3/envs/anjenv/Lib/site-packages/ocr-convert-image-to-text-master/sample/ocr1.jpg')
#os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'C:/Users/ANJALI/Desktop/My Project 33415-148adae0ebee.json' #give path to your Service account keys .json file
#bq_client = Client()
#path='C:/Users/ANJALI/Anaconda3/envs/anjenv/Lib/site-packages/ocr-convert-image-to-text-master/sample/file-page1.jpg'    					  #give path to your image
#detect_text(path)