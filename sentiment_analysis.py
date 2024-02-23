# pylint: disable=missing-docstring
"""
this is pointing a gun at my head to make a docstring, so I make docstring 
"""

import requests

def sentiment_analyzer(text_to_analyse):
    try:
        url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
        header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
        myobj = {"raw_document": {"text": text_to_analyse}}
        response = requests.post(url, json = myobj, headers = header, timeout=10)
        return response.text
    except requests.exceptions.RequestException as e:
        print("Error", e)
