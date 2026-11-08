from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/emotionDetector')
def emotion_detector_route():
    text_to_analyze = request.args.get('textToAnalyze')
    result = emotion_detector(text_to_analyze)

    # Check if dominant emotion is None
    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    return result

if __name__ == '__main__':
    app.run(host='localhost', port=5000)