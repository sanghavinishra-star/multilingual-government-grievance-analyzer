# Multilingual Government Grievance Analyzer

## Project Overview

The Multilingual Government Grievance Analyzer is an AI-based system that analyzes citizen complaints written in English or Marathi.

It classifies complaints, detects urgency, and routes them to the appropriate government department.

## Features

- English and Marathi complaint support
- Complaint category classification
- Urgency detection
- Automatic department routing
- Machine learning based text classification
- Gradio web interface

## Categories

- Water
- Electricity
- Roads
- Sanitation
- Healthcare
- Public Safety

## Workflow

Complaint -> Category Prediction -> Urgency Detection -> Department Routing -> Final Result

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- TF-IDF
- Logistic Regression
- Joblib
- Gradio
- Google Colab
- GitHub

## Dataset

The project uses a synthetic/demo dataset containing 120 complaint examples in English and Marathi.

The dataset covers six complaint categories with urgency and department information.

## Model Results

| Component | Accuracy |
|---|---:|
| Category Classification | 66.67% |
| Urgency Detection | 37.50% |
| Department Model | 62.50% |

Note: The dataset is relatively small and synthetic, so these results are intended for academic demonstration rather than real-world government deployment.

## Department Routing

- Water -> Water Supply Department
- Electricity -> Electricity Department
- Roads -> Road Department
- Sanitation -> Sanitation Department
- Healthcare -> Health Department
- Public Safety -> Police Department

## Sample Input

English:

There is no electricity in my area and the power has been out for hours.

Expected result:

Category: Electricity  
Urgency: High  
Department: Electricity Department

Marathi:

माझ्या भागात पाणी येत नाही आणि अनेक दिवसांपासून पाणीपुरवठा बंद आहे

Expected result:

Category: Water  
Urgency: High  
Department: Water Supply Department

## Project Files

- app.py - Main application
- category_model.pkl - Category classification model
- urgency_model.pkl - Urgency detection model
- department_model.pkl - Department classification model
- requirements.txt - Required Python libraries
- README.md - Project documentation

## How to Run

Install the required libraries:

pip install -r requirements.txt

Run the application:

python app.py

## Future Scope

- Add more Indian languages
- Use a larger real-world grievance dataset
- Improve urgency detection
- Add multilingual transformer models
- Add complaint history and tracking
- Connect with real government grievance portals

## Conclusion

The Multilingual Government Grievance Analyzer demonstrates how machine learning and natural language processing can be used to automatically analyze citizen complaints and assist in routing them to relevant departments.
