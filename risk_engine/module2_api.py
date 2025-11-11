from flask import Flask, request, jsonify
from flask_cors import CORS 
app = Flask(__name__)
CORS(app)  
print("--- MODULE 2: Ready for questionnaire scoring. ---")


def score_phq9(answers):
    """Calculates and interprets the PHQ-9 depression score."""
    score = sum(answers)
    level = "minimal depression"
    if 5 <= score <= 9: level = "mild depression"
    elif 10 <= score <= 14: level = "moderate depression"
    elif 15 <= score <= 19: level = "moderately severe depression"
    elif score >= 20: level = "severe depression"
    return {"questionnaire": "PHQ-9", "risk_score": score, "level": level}

def score_gad7(answers):
    """Calculates and interprets the GAD-7 anxiety score."""
    score = sum(answers)
    level = "minimal anxiety"
    if 5 <= score <= 9: level = "mild anxiety"
    elif 10 <= score <= 14: level = "moderate anxiety"
    elif score >= 15: level = "severe anxiety"
    return {"questionnaire": "GAD-7", "risk_score": score, "level": level}

@app.route('/score/questionnaire', methods=['POST'])
def handle_questionnaire():
    data = request.get_json()
    q_type = data.get('type', '').lower()
    answers = data.get('answers', [])

    if not all(isinstance(i, int) for i in answers):
        return jsonify({"error": "Answers must be a list of integers."}), 400

    if q_type == 'phq9' and len(answers) == 9:
        result = score_phq9(answers)
    elif q_type == 'gad7' and len(answers) == 7:
        result = score_gad7(answers)
    else:
        return jsonify({"error": "Invalid questionnaire type or wrong number of answers."}), 400
        
    return jsonify(result)


if __name__ == '__main__':

    app.run(debug=True, port=5002)