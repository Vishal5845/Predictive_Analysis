# Machine Learning with Django

This project contains a web application built using the Django framework that integrates machine learning models to provide predictive analytics. The application allows users to input data through a web interface, which is then processed by a machine learning model to generate predictions.

## Project Structure
The repository is organized as follows:

- `DiabetesPrediction/`: The main Django project directory containing settings, configurations, views and templates related to the machine learning feature.
- `static/`: Static files images used in the application.
- `templates/`: HTML templates for rendering the web pages.
- `README.md`: Project overview and setup instructions.

## Features
- **User Interface:** A web-based interface to input data and view predictions.
- **Machine Learning Models:** Pre-trained models for making predictions based on user input.

## Installation

### Prerequisites
- Python3
- Django
- Virtual environment setup (optional but recommended)

### Steps   

1. Create and activate a virtual environment:
   python3 -m venv venv
   source venv/bin/activate

2. Install dependencies:
   pip install -r requirements.txt

3. Apply migrations:
   python manage.py migrate

4. Run the development server:
   python manage.py runserver

5. Access the application:
   Open your web browser and navigate to http://127.0.0.1:8000/