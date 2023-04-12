 # berikut kodel program prediksi.py
import tensorflow
from tensorflow import keras
from keras.models import load_model
import cv2
import numpy as np

def predict(img):
    # lakukan prediksi pada numpy array
    model = load_model("model_5")
    y_pred = model.predict(np.expand_dims(img, axis=0))
    y_pred = int(np.argmax(y_pred, axis=1))

    return y_pred