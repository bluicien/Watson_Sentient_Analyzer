'''This module contains the function for finding the sentiment in the user input
'''

import json
import requests

def sentiment_analyzer(text_to_analyse):
    ''' This function takes in user input and passes it to the Watson AI to analyze
        the sentiment in the input and output the sentiment type and trust score.
    '''

    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    headers = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = myobj, headers=headers)
    resp_dict = json.loads(response.text)
    if response.status_code == 500:
        label = None
        score = None
    else:
        label = resp_dict['documentSentiment']['label']
        score = resp_dict['documentSentiment']['score']
    return {'Label' : label, 'Score': score}
