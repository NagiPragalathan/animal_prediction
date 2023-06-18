# Animal Prediction

[![Python](https://img.shields.io/badge/Python-3.9-blue)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-3.2-green)](https://www.djangoproject.com/)

Animal Prediction is a web application developed using Python and Django that allows users to predict the animal species based on uploaded photos. The application utilizes machine learning algorithms to analyze the image data and provide accurate predictions.

## Features

- User-friendly web interface for uploading animal photos.
- Machine learning model trained on a dataset of various animal species.
- Predictive analysis to determine the most probable animal species in the uploaded photo.
- Visual representation of prediction results with confidence scores.

## Installation

Follow these steps to set up and run the Animal Prediction web application locally:

1. Clone the repository:

   ```shell
   git clone https://github.com/NagiPragalathan/animal_prediction.git
   ```
2. Navigate to the project directory:
    
    
    `cd animal_prediction` 
    
3. Create a virtual environment:
    
    
    `python -m venv env` 
    
4. Activate the virtual environment:
    
    - For Windows:
        
        
        `env\Scripts\activate` 
        
    - For macOS/Linux:
        
        `source env/bin/activate` 
        
5. Install the dependencies:
    
    
    `pip install -r requirements.txt` 
    
6. Run database migrations:
    
    `python manage.py migrate` 
    
7. Start the development server:
    
    
    `python manage.py runserver` 
    
8. Open a web browser and access the application at `http://localhost:8000`.
    

## Usage

1. On the home page, click on the "Upload Photo" button to select an animal photo from your device.
    
2. After selecting the photo, click on the "Predict" button to perform the animal prediction analysis.
    
3. Wait for the analysis to complete. The application will display the predicted animal species along with a confidence score.
    
4. You can upload multiple photos and perform predictions for each of them.
    

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or bug reports, please open an issue on the GitHub repository.

## License

This project is licensed under the [MIT License]().
