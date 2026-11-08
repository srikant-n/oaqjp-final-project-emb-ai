import requests
import json

# Function to analyze emotions in text
def emotion_detector(text_to_analyze):
    """
    Analyze emotions in the given text using the Watson NLP API.
    
    Args:
        text_to_analyze (str): The text to analyze for emotions.
    
    Returns:
        dict: A dictionary containing the emotion scores and the dominant emotion.
    """

    # Define the URL and headers
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    # Create the input JSON
    input_json = { "raw_document": { "text": text_to_analyze } }
    # Make the POST request
    response = requests.post(url, headers=headers, json=input_json)
    response = response.json()

    # Extract the emotions from the response
    result = {
        'anger': response['emotionPredictions'][0]['emotion']['anger'],
        'disgust': response['emotionPredictions'][0]['emotion']['disgust'],
        'fear': response['emotionPredictions'][0]['emotion']['fear'],
        'joy': response['emotionPredictions'][0]['emotion']['joy'],
        'sadness': response['emotionPredictions'][0]['emotion']['sadness'],
    }
    result['dominant_emotion'] = max(result, key=result.get)
    return result