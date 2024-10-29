# 🍋 Lemon Quality Detection

This project is a web application built with Django to detect and classify the quality of lemons based on various features. The application uses a trained machine learning model to predict lemon quality, which can be helpful for food processing industries, quality control labs, and agricultural studies. 

## Features
- **Upload Lemon Image**: Users can upload images of lemons to get quality predictions.
- **Model Prediction**: Leverages a trained ML model (CNN) to analyze lemon quality.
- **History**: Saves prediction history for users to track past analyses.
- **Admin Panel**: Django admin interface to manage users and analyze the dataset.

## Technology Stack
- **Backend**: Django
- **Frontend**: HTML, CSS, JavaScript (optional: Bootstrap for styling)
- **Machine Learning Model**: Convolutional Neural Network (CNN) trained using TensorFlow/Keras
- **Database**: SQLite (default, can be switched to PostgreSQL or MySQL for production)

## Project Setup

### Prerequisites
- Python 3.8+
- Django 4.x
- TensorFlow 2.x
- OpenCV (for image processing)
  
### Installation

1. **Clone the Repository**
    ```bash
    git clone https://github.com/nisch-mhrzn/Lemon-Quality-Detection.git
    cd lemon-quality-detection
    ```

2. **Create a Virtual Environment**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run Migrations**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Start the Django Development Server**
    ```bash
    python manage.py runserver
    ```

6. **Access the Application**
    Open [http://localhost:8000](http://localhost:8000) in your browser to view the application.

### Model Integration
1. **Prepare the Model**: Ensure the trained CNN model (saved as `lemon_quality_model.h5`) is in the `models` directory.
2. **Load Model in Django App**: The model is loaded into Django via TensorFlow to make predictions on uploaded images.

## Usage
1. **Upload an Image**: On the main page, users can upload an image of a lemon for quality assessment.
2. **Get Predictions**: The application analyzes the image and returns the predicted quality (e.g., "Good Quality," "Empty Background," "Bad Quality").
3. **View History**: Users can view their past predictions in the history section.

## Folder Structure
```plaintext
lemon-quality-detection/
├── home/         # Main Django app for lemon quality detection
├── models/                    # Folder for storing machine learning models
├── static/                    # Static files (CSS, JS, images)
├── templates/                 # HTML templates
├── README.md
└── requirements.txt
```


## Contributing
Contributions are welcome! Feel free to submit a Pull Request for bug fixes or feature enhancements.
