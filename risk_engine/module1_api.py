import joblib
from flask import Flask, request, jsonify
from flask_cors import CORS
import re
import nltk
from transformers import pipeline
import warnings
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


warnings.filterwarnings("ignore", category=UserWarning, module='transformers')
app = Flask(__name__)
CORS(app)


print("--- MODULE 1: Loading all models. This may take a moment. ---")

try:
    vectorizer = joblib.load('../scripts/tfidf_vectorizer.pkl')
    custom_model = joblib.load('../scripts/risk_classifier_model.pkl')
    print("Custom risk classifier and vectorizer loaded successfully.")
    
    sentiment_pipeline = pipeline("sentiment-analysis", model="cardiffnlp/twitter-roberta-base-sentiment-latest")
    print("General sentiment model loaded successfully.")
except FileNotFoundError:
    print("FATAL ERROR: Model files not found. Please ensure they are in the 'scripts' folder.")
    exit()
except Exception as e:
    print(f"FATAL ERROR: Could not load models. Error: {e}")
    exit()


def preprocess_text(text):
    if not isinstance(text, str):
        return ""
    lemmatizer = WordNetLemmatizer()
    stop_words = set(stopwords.words('english'))
    text = text.lower()
    text = re.sub(r"[^a-zA-Z\s']", '', text)
    tokens = text.split()
    processed_tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in stop_words]
    return ' '.join(processed_tokens)


@app.route('/analyze', methods=['POST'])
def analyze_text():
    data = request.get_json()
    if not data or 'text' not in data:
        return jsonify({"error": "Invalid input. Please provide JSON with a 'text' key."}), 400

    text_input = data['text']
    
    sentiment_result = sentiment_pipeline(text_input)[0]
    sentiment_label = sentiment_result['label'].lower()
    confidence = round(sentiment_result['score'], 2)

    processed_input = preprocess_text(text_input)
    vectorized_input = vectorizer.transform([processed_input])
    custom_prediction = custom_model.predict(vectorized_input)[0]
    tone = 'high-risk' if custom_prediction == 'suicide' else 'low-risk'

    processed_word_count = len(processed_input.split())
    
    if tone == 'high-risk' and sentiment_label == 'positive' and processed_word_count <= 2:
        
        tone = 'low-risk'
    

    final_output = {
        "text": text_input,
        "sentiment": sentiment_label,
        "tone": tone,
        "confidence_score": confidence
    }
    return jsonify(final_output)


if __name__ == '__main__':

    try:
        nltk.data.find('corpora/stopwords')
        nltk.data.find('corpora/wordnet')
    except LookupError:
        nltk.download('stopwords')
        nltk.download('wordnet')
    

    app.run(debug=True, port=5001)