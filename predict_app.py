import base64
import numpy as np
import io
from PIL import Image
from keras.preprocessing.image import  img_to_array, image
from flask import request,jsonify, Flask
import tensorflow as tf

app = Flask(__name__)

def get_model():
    global model
    model = tf.keras.models.load_model("model.h5")
    print("* Model loaded!")

def preprocess_image(image): #image preprocessing 
    image= img_to_array(image)
    image = np.dot(image[...,:3], [0.2989,0.5870,0.1140]) #converting image to black&white
    image =  image[165:470,270:340] #slecting the SMN1-coresponding region of the image
    image = image/255.0
    image = image.reshape(305,70,1) #adds the third dimension
    image = np.expand_dims(image, axis = 0) #adds the fourth dimension
    return image

print("* Loading Keras model....")

get_model()

@app.route("/predict", methods=["POST"])
def predict():
    message = request.get_json(force=True)
    encoded = message['image']
    decoded = base64.b64decode(encoded)
    image = Image.open(io.BytesIO(decoded))
    processed_image = preprocess_image(image) #preprocess the image with the above function

    prediction = model.predict(processed_image)
    for i in prediction:
        if float(prediction[0]) > 0.5:
            response = "The sample is SMA negative, the certainty is "+str(round(float(prediction[0])*100,2))+"%"
        else:
            response = "The sample is SMA positive, the certainty is "+str(round((1-float(prediction[0]))*100,2))+"%"
    return jsonify(response)
