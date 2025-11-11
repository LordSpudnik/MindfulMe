Project README: How to Run
1. Assumed Folder Structure
Your Python scripts use relative paths (like ../data/ and ../scripts/). For this to work, your project must be organized like this:

project-folder/
├── data/
│   ├── raw/
│   │   └── suicide_detection_data.csv
│   └── processed/
├── frontend/
│   ├── login_page.html
│   ├── expression_page.html
│   └── ...
├── risk_engine/
│   ├── module1_api.py
│   ├── module2_api.py
│   ├── data_preprocessor.py
│   └── final_analyzer.py
└── scripts/
    (This folder starts empty)
2. One-Time-Only Setup
Step 2.1: Install Dependencies
Install all required Python libraries.

Bash

# Install all required libraries
pip install flask flask-cors pandas nltk scikit-learn joblib transformers torch
Step 2.2: Prepare NLTK Data
The scripts require NLTK data. Run this in your terminal:

Bash

python -c "import nltk; nltk.download('stopwords'); nltk.download('wordnet')"
Step 2.3: Process Raw Data
Navigate into the risk_engine folder.

Bash

cd risk_engine
Now, run the preprocessor. It will read from ../data/raw/ and save to ../data/processed/.

Bash

# This script reads 'suicide_detection_data.csv' and creates 'processed_suicide_data.csv'
python data_preprocessor.py
Step 2.4: Train and Place the Models (CRITICAL)
While still in the risk_engine folder, run the analyzer.

Bash

# This script uses 'processed_suicide_data.csv' to create
# 'tfidf_vectorizer.pkl' and 'risk_classifier_model.pkl'
python final_analyzer.py
This saves the .pkl files inside risk_engine. You must move them to the scripts folder.

Bash

# Move the two new model files up one level and into the 'scripts' folder
mv tfidf_vectorizer.pkl ../scripts/
mv risk_classifier_model.pkl ../scripts/
3. How to Run the Application
You must have three separate terminals open.

Terminal 1: Run Module 1 (Analysis API)
Navigate to the risk_engine folder and run the first server.

Bash

cd /path/to/project-folder/risk_engine
python module1_api.py
Wait for it to load the models (it will say http://localhost:5001).

Terminal 2: Run Module 2 (Quiz API)
Navigate to the risk_engine folder and run the second server.

Bash

cd /path/to/project-folder/risk_engine
python module2_api.py
This will run on http://localhost:5002.

Terminal 3: Run Frontend Server
Navigate to the frontend folder and run the web server.

Bash

cd /path/to/project-folder/frontend
python -m http.server 8000
This will serve your HTML files on http://localhost:8000.

4. Access the Application
Once all three servers are running:

Open your web browser (e.g., Chrome, Firefox).

Go to this exact URL: http://localhost:8000/login_page.html

Do NOT double-click the HTML file from your file explorer.