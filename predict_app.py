import base64
import numpy as np
import io
from PIL import Image
from keras.preprocessing.image import  img_to_array, image
from flask import request,jsonify, Flask
import tensorflow as tf

app = Flask(__name__)

def get_model(): #funkcija koja ucitava model
    global model
    model = tf.keras.models.load_model("model_za_flask.h5")
    print("* Model loaded!")

def preprocess_image(image): #obrada slike, da bi bila ista kao u treningu
    image= img_to_array(image) #konvertuje u matricu
    image = np.dot(image[...,:3], [0.2989,0.5870,0.1140]) #prebacuje u crno-belu
    image =  image[165:470,270:340] #isece odgovarajuci deo
    image = image/255.0 #normalizacija
    image = image.reshape(305,70,1) #dodaje trecu dimenziju (1 posto je crno-bela)
    image = np.expand_dims(image, axis = 0) #dodaje jos jednu dimenziju
    return image

print("* Loading Keras model....")

get_model()

@app.route("/predict", methods=["POST"])
def predict():
    message = request.get_json(force=True)
    encoded = message['image']
    decoded = base64.b64decode(encoded) #prebacuje sliku u odgovarajuci oblik
    image = Image.open(io.BytesIO(decoded))
    processed_image = preprocess_image(image) #obradjuje sliku

    prediction = model.predict(processed_image)  #predvidjanje - daje verovatnocu
    for i in prediction:
        if float(prediction[0]) > 0.5:  #po kljucu 0:SMA+ ; 1:SMA-
            response = "Osoba je SMA negativna, sigurnost predviđanja je "+str(round(float(prediction[0])*100,2))+"%"
        else:
            response = "Osoba je SMA pozitivna, sigurnost predviđanja je "+str(round((1-float(prediction[0]))*100,2))+"%"
    return jsonify(response)