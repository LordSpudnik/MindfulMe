# MindfulMe

MindfulMe is a compassionate, data-powered platform designed to help users understand and improve their mental wellbeing. It combines frontend interactivity, backend analytics, and machine learning to provide risk detection and engaging activities for users.

## Features

- Modern, user-friendly web interface for login and emotional tracking
- In-depth risk analysis powered by trained ML models
- Interactive quizzes to personalize recommendations
- Modular Python backend APIs (Flask)
- Data preprocessing and model training scripts

## Getting Started

### Prerequisites

- Python 3.8+
- pip
- Modern web browser

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/LordSpudnik/MindfulMe.git
   cd MindfulMe
   ```

2. **Install dependencies:**

   ```bash
   pip install flask flask-cors pandas nltk scikit-learn joblib transformers torch
   ```

3. **Download required NLTK datasets:**

   ```bash
   python -c "import nltk; nltk.download('stopwords'); nltk.download('wordnet')"
   ```

### Folder Structure

```
MindfulMe/
├── data/
│   ├── raw/                # Raw source data
│   └── processed/          # Preprocessed data
├── frontend/               # Web HTML pages
├── risk_engine/            # Python backend and ML models
├── scripts/                # Model pickle files
└── README.md
```

### Preparing Data and Models

1. **Process raw data:**

   ```bash
   cd risk_engine
   python data_preprocessor.py
   ```
   _Creates processed data file in `../data/processed/`._

2. **Train and export models:**

   ```bash
   python final_analyzer.py
   ```
   _Generates `tfidf_vectorizer.pkl` and `risk_classifier_model.pkl` in `risk_engine/`._

3. **Move model files to `scripts/`:**

   ```bash
   mv tfidf_vectorizer.pkl ../scripts/
   mv risk_classifier_model.pkl ../scripts/
   ```

## Running MindfulMe

You’ll need three terminals:

1. **Terminal 1 — Risk Analysis API:**

   ```bash
   cd risk_engine
   python module1_api.py
   ```
   _Runs at http://localhost:5001_

2. **Terminal 2 — Quiz API:**

   ```bash
   cd risk_engine
   python module2_api.py
   ```
   _Runs at http://localhost:5002_

3. **Terminal 3 — Frontend:**

   ```bash
   cd frontend
   python -m http.server 8000
   ```
   _Visit http://localhost:8000/login_page.html in your browser_

## Usage

- Complete login and quizzes via frontend
- System analyzes data, providing feedback and risk alerts
- All processing is local for privacy (no data sent externally)
