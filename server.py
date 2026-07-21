"""
Flask application for detecting emotions from user input.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    """
    Analyze the given text and return emotion predictions.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    result = ""

    for emotion, score in response.items():
        if emotion != "dominant_emotion":
            result += f"'{emotion}': {score}, "

    result = result.rstrip(", ")

    dominant = response['dominant_emotion']

    if dominant is None:
        return "Invalid Text! Please try again!"

    return (
        f"For the given statement the system response is {result}." 
        f"The dominant emotion is {dominant}"
    )

@app.route("/")
def render_index_page():
    """
    Render the home page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
       