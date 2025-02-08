import requests
import json

def sentiment_analyzer(text_to_analyse):
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json=myobj, headers=header)
    response_json = response.json()  # Access the JSON content

    # label = response_json['documentSentiment']['label']
    # score = response_json['documentSentiment']['score']
    formatted_response = {
        "label": response_json['documentSentiment']['label'],
        "score": response_json['documentSentiment']['score']
    }
    
    return formatted_response