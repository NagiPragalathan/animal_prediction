from .animal_predictor import predict_animal1
import io
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
import base64


def login_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print(user,"sample")
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('login')
    return render(request,'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to a desired page after logout


def signup_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        User.objects.create_user(username=username, password=password)
        return redirect('/login')
    return render(request,'signup.html')

def home(request):
    return render(request,'home.html')

# Example usage in Django view
def predict(request):
    if request.method == 'POST' and request.FILES['image']:
        image_file = request.FILES['image']
        animal = predict_animal1(io.BytesIO(image_file.read()))
        return render(request, 'getImage.html', {'animal': animal})
    return render(request, 'getImage.html')

from django.shortcuts import render
from django.http import JsonResponse
import numpy as np
import cv2
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model

# Load the pre-trained model
model = load_model('animals.h5')

# Define the class names associated with the animals
class_names = ['butterfly', 'cat', 'chicken', 'cow', 'dog', 'elephant', 'horse', 'sheep', 'spider', 'squirrel']


# Function to predict animal in an image
def predict_animal(frame):
    try:
        frame = cv2.resize(frame, (224, 224))  # Resize the frame to the desired input size
        img = image.img_to_array(frame)
        img = np.expand_dims(img, axis=0)
        img = img / 255.0  # Normalize the image
        prediction = model.predict(img)
        output = np.argmax(prediction)
        predicted_class = class_names[output]
        print(predicted_class)
        predicted_prob = float(np.max(prediction))  # Convert to regular float
        return predicted_class, predicted_prob
    except Exception as e:
        print("Error predicting animal:", str(e))
        return None, None


def process_video_frame(request):
    if request.method == 'POST':
        # Process the video frame data here
        # Extract the frame data from the POST request
        frame_data = request.POST.get('frame_data')

        # Decode the base64-encoded frame data
        _, encoded_data = frame_data.split(',')
        decoded_data = base64.b64decode(encoded_data)

        # Convert the decoded data to a numpy array
        nparr = np.frombuffer(decoded_data, np.uint8)
        frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        # Predict animal
        predicted_animal, predicted_prob = predict_animal(frame)

        # Draw a rectangle around the predicted animal on the canvas
        if predicted_animal is not None:
            height, width, _ = frame.shape
            cv2.rectangle(frame, (0, 0), (width, height), (0, 255, 0), 2)

        # Return the response
        response_data = {
            'animal': predicted_animal,
            'probability': predicted_prob
        }
        return JsonResponse(response_data)

    return render(request, 'video.html')
