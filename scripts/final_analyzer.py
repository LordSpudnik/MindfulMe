import pandas as pd
import re
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from transformers import pipeline
import joblib 
import warnings

warnings.filterwarnings("ignore", category=UserWarning, module='transformers')

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')
try:
    nltk.data.find('corpora/wordnet')
except LookupError:
    nltk.download('wordnet')

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

def preprocess_text(text):
    if not isinstance(text, str):
        return ""
    lemmatizer = WordNetLemmatizer()
    stop_words = set(stopwords.words('english'))
    text = text.lower()
    text = re.sub(r"[^a-zA-Z\s']", '', text)
    tokens = text.split()
    processed_tokens = [
        lemmatizer.lemmatize(word) for word in tokens if word not in stop_words
    ]
    return ' '.join(processed_tokens)

if __name__ == "__main__":
    processed_data_path = '../data/processed/processed_suicide_data.csv'
    output_results_path = '../data/results/analysis_results.csv'
    vectorizer_save_path = './tfidf_vectorizer.pkl'
    model_save_path = './risk_classifier_model.pkl'

    print("--- Training Custom Risk Classifier ---")
    try:
        df = pd.read_csv(processed_data_path)
        df.dropna(subset=['processed_text', 'class'], inplace=True)
        
        vectorizer = TfidfVectorizer(max_features=5000)
        X_tfidf = vectorizer.fit_transform(df['processed_text'])
        y = df['class']
        
        custom_model = LogisticRegression(max_iter=1000)
        custom_model.fit(X_tfidf, y)
        print("Custom classifier trained successfully.")

        joblib.dump(vectorizer, vectorizer_save_path)
        print(f"Vectorizer saved to {vectorizer_save_path}")
        joblib.dump(custom_model, model_save_path)
        print(f"Model saved to {model_save_path}")
        
    except FileNotFoundError:
        print(f"Error: Processed data not found at {processed_data_path}. Please run the preprocessor first.")
        exit()

    print("\n--- Loading General Sentiment Model ---")
    sentiment_pipeline = pipeline("sentiment-analysis", model="cardiffnlp/twitter-roberta-base-sentiment-latest")
    print("General sentiment model loaded.")

    def analyze_text_holistically(text_input):
        sentiment_result = sentiment_pipeline(text_input)[0]
        sentiment_label = sentiment_result['label'].lower()
        confidence = round(sentiment_result['score'], 2)
        processed_input = preprocess_text(text_input)
        vectorized_input = vectorizer.transform([processed_input])
        custom_prediction = custom_model.predict(vectorized_input)[0]
        tone = 'high-risk' if custom_prediction == 'suicide' else 'low-risk'
        return {"text": text_input, "sentiment": sentiment_label, "tone": tone, "confidence_score": confidence}

    print("\n--- Running Analysis on New Sentences ---")
    example_texts = [
        "I'm feeling really down and hopeless today, I don't think I can go on.",
        "I need help, everything just feels so pointless.",
        "Finally finished my project, what a relief! It was a good day.",
        "I am so tired of everything."
    ]
    results_list = [analyze_text_holistically(text) for text in example_texts]
    results_df = pd.DataFrame(results_list)
    results_df.to_csv(output_results_path, index=False)
    print("Analysis complete. Results saved successfully!")