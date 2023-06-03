import io
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model

# Load the pre-trained model
model = load_model('animals.h5')

# Define the class names associated with the animals
class_names = ['butterfly', 'cat', 'chicken', 'cow', 'dog', 'elephant', 'horse', 'sheep', 'spider', 'squirrel']

# Function to predict animal in an image
def predict_animal1(image_file):
    img = Image.open(image_file)
    img = img.resize((224, 224))
    img = image.img_to_array(img)
    img = img.reshape((1, 224, 224, 3))
    img = img / 255.0  # Normalize the image
    prediction = model.predict(img)
    output = np.argmax(prediction)
    return class_names[output]
