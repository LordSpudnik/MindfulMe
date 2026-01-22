# MindfulMe 🧠💬  
MindfulMe is a **privacy-preserving mental health assessment system** that performs **sentiment analysis**, **suicide risk detection**, and **standard mental health questionnaire scoring** **entirely on the user's local machine**.

---

## 📌 Key Features

✅ **Hybrid Text Analysis (Module 1 - NLP + Risk Detection)**  
- General sentiment classification using a Hugging Face transformer model  
- Suicide risk detection using a custom ML model trained on TF-IDF + Logistic Regression  
- Returns:
  - `sentiment` → positive / neutral / negative  
  - `tone` → high-risk / low-risk  
  - `confidence_score`

✅ **Clinical Questionnaire Scoring (Module 2)**  
Automated scoring for:
- **PHQ-9 (Depression)**
- **GAD-7 (Anxiety)**  
Returns total score + severity category.

✅ **Frontend UI (Static HTML + TailwindCSS)**  
A lightweight multi-page UI (without frameworks) that interacts with Flask APIs using fetch.

---

## 🏗️ Project Structure

```bash
MindfulMe/
│
├── data/
│   ├── raw/
│   │   └── suicide_detection_data.csv
│   ├── processed/
│   │   └── processed_suicide_data.csv
│   └── results/
│       └── analysis_results.csv
│
├── risk_engine/
│   ├── module1_api.py
│   └── module2_api.py
│
├── scripts/
│   ├── data_preprocessor.py
│   ├── final_analyzer.py
│   ├── risk_classifier_model.pkl
│   └── tfidf_vectorizer.pkl
│
├── ui/
│   ├── login_page.html
│   ├── expression_page.html
│   ├── decision_page.html
│   ├── questionnaire.html
│   └── stats_page.html
│
├── AI Powered Chatbots for Mental Health Assessment and Support.pdf
├── README.md
└── requirements.txt
```

## ⚙️ Tech Stack

Python

Flask + Flask-CORS

Hugging Face Transformers

Scikit-learn

Pandas / NumPy

NLTK

HTML + TailwindCSS + JavaScript

## 🚀 How It Works (Workflow)

🔹 Module 1: Text Sentiment + Suicide Risk Detection (Port 5001)

User enters a message in the UI

UI calls: POST http://localhost:5001/analyze

API returns:

sentiment label (transformer)

high-risk/low-risk tone (custom model)

confidence score

🔹 Module 2: Questionnaire Scoring (Port 5002)

User answers PHQ-9 / GAD-7

UI calls: POST http://localhost:5002/score/questionnaire

API returns:

total score

severity level


## 🔌 API Usage
✅ Module 1: Analyze Text

Endpoint

POST /analyze


Example Request

{
  "text": "I feel very hopeless and tired of everything."
}


Example Response

{
  "text": "I feel very hopeless and tired of everything.",
  "sentiment": "negative",
  "tone": "high-risk",
  "confidence_score": 0.92
}

✅ Module 2: Score Questionnaire (PHQ-9 or GAD-7)

Endpoint

POST /score/questionnaire

PHQ-9 Example
{
  "type": "phq9",
  "answers": [1,2,0,1,2,1,0,1,1]
}

GAD-7 Example
{
  "type": "gad7",
  "answers": [0,1,1,2,0,1,2]
}


Example Response

{
  "questionnaire": "PHQ-9",
  "risk_score": 9,
  "level": "mild depression"
}

## 🧪 Training / Reproducing the Model (Optional)
✅ Step 1: Preprocess the raw dataset
cd scripts
python data_preprocessor.py


Input:

data/raw/suicide_detection_data.csv

Output:

data/processed/processed_suicide_data.csv

✅ Step 2: Train the custom risk classifier
python final_analyzer.py


Outputs:

scripts/tfidf_vectorizer.pkl

scripts/risk_classifier_model.pkl

## 📄 Research Paper (Unpublished)

This repository includes the unpublished research paper:

📌 AI Powered Chatbots for Mental Health Assessment and Support.pdf

## ⚠️ Disclaimer

This paper is currently unpublished and is shared here for academic and project reference purposes only.

Do not reuse, reproduce, or redistribute this paper without explicit permission from the authors.
All rights reserved © 2026.

## 🛡️ Safety & Ethical Disclaimer (Important)

MindfulMe is intended for educational and research purposes only.

✅ This project is NOT a medical device
✅ This project does NOT provide clinical diagnosis
✅ Users should consult licensed professionals for real support

If you or someone you know is in immediate danger or distress, please contact local emergency services or a verified crisis hotline.

## 👨‍💻 Authors

Akilan VS
Subash Venkat
Muhibullah

VIT Chennai

## 📌 License

Paper (PDF): All Rights Reserved
