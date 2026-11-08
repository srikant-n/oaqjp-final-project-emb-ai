import pytest
from EmotionDetection import emotion_detector

def test_emotion_joy():
    result = emotion_detector("I am glad this happened")
    assert result['dominant_emotion'] == 'joy'


def test_emotion_anger():
    result = emotion_detector("I am really mad about this")
    assert result['dominant_emotion'] == 'anger'

def test_emotion_disgust():
    result = emotion_detector("I feel disgusted just hearing about this")
    assert result['dominant_emotion'] == 'disgust'

def test_emotion_sadness():
    result = emotion_detector("I am so sad about this")
    assert result['dominant_emotion'] == 'sadness'

def test_emotion_fear():
    result = emotion_detector("I am really afraid that this will happen")
    assert result['dominant_emotion'] == 'fear'
