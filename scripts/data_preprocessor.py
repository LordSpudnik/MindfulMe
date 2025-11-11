import pandas as pd
import re
import nltk

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    print("Downloading 'stopwords' package...")
    nltk.download('stopwords')
try:
    nltk.data.find('corpora/wordnet')
except LookupError:
    print("Downloading 'wordnet' package...")
    nltk.download('wordnet')

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

print("Libraries imported and NLTK data is ready.")

def preprocess_text(text, line_num):
    if not isinstance(text, str):
        print("  [STEP 0] Input is not a string. Skipping.")
        return ""

    try:
        fixed_text = text.encode('latin-1').decode('utf-8', errors='replace')
    except Exception as e:
        print(f"  [STEP 1] FAILED Encoding Fix: {e}")
        fixed_text = text 
    
    lower_text = fixed_text.lower()

    regex_text = re.sub(r"[^a-zA-Z\s']", '', lower_text)
    
    lemmatizer = WordNetLemmatizer()
    stop_words = set(stopwords.words('english'))
    tokens = regex_text.split()
    processed_tokens = [
        lemmatizer.lemmatize(word) for word in tokens if word not in stop_words
    ]
    final_text = ' '.join(processed_tokens)

    return final_text

if __name__ == "__main__":
    raw_data_path = '../data/raw/suicide_detection_data.csv'
    processed_data_path = '../data/processed/processed_suicide_data.csv'

    print(f"\nReading raw data from: {raw_data_path}")
    
    try:
        texts = []
        classes = []
        with open(raw_data_path, 'r', encoding='latin-1') as f:
            header = next(f) 
            for i, line in enumerate(f, 2):
                try:
                    parts = line.rsplit(',', 1)
                    if len(parts) == 2:
                        texts.append(parts[0])
                        classes.append(parts[1].strip())
                    else:
                        ...
                except Exception as e:
                    ...

        df = pd.DataFrame({'text': texts, 'class': classes})
        print("\nRaw data manually loaded. Now starting detailed preprocessing...")

        processed_texts = []
        for i, text in enumerate(df['text'], 2): 
            processed_texts.append(preprocess_text(text, i))
        
        df['processed_text'] = processed_texts
        
        print("\n\n----- PREPROCESSING COMPLETE -----")

        df.to_csv(processed_data_path, index=False)
        print(f"\nProcessed data saved to: {processed_data_path}")
        
    except FileNotFoundError:
        print(f"Error: The file was not found at {raw_data_path}. Please check the path.")