
import joblib
import gradio as gr

# Load trained models
category_model = joblib.load("category_model.pkl")
urgency_model = joblib.load("urgency_model.pkl")

# Department mapping
department_mapping = {
    "Water": "Water Supply Department",
    "Electricity": "Electricity Department",
    "Roads": "Road Department",
    "Sanitation": "Sanitation Department",
    "Healthcare": "Health Department",
    "Public Safety": "Police Department"
}

def analyze_grievance(complaint):
    category = category_model.predict([complaint])[0]
    urgency = urgency_model.predict([complaint])[0]
    department = department_mapping[category]

    return {
        "Category": category,
        "Urgency": urgency,
        "Department": department
    }

def predict_grievance(complaint):
    if not complaint.strip():
        return "Please enter a complaint.", "", ""

    result = analyze_grievance(complaint)

    return (
        result["Category"],
        result["Urgency"],
        result["Department"]
    )

# Gradio interface
demo = gr.Interface(
    fn=predict_grievance,
    inputs=gr.Textbox(
        lines=4,
        placeholder="Enter a government complaint in English or Marathi..."
    ),
    outputs=[
        gr.Textbox(label="Category"),
        gr.Textbox(label="Urgency"),
        gr.Textbox(label="Department")
    ],
    title="Multilingual Government Grievance Analyzer",
    description="Classifies complaints, detects urgency, and routes them to the appropriate department."
)

demo.launch()
