import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, KeywordsOptions

def keywords(text_value):
    authenticator = IAMAuthenticator('l-N-7Ay2cS2xMSaA527WXej4o5kYdjIJrANlF9ndK6RG')
    natural_language_understanding = NaturalLanguageUnderstandingV1(
        version='2021-08-01',
        authenticator=authenticator
    )

    natural_language_understanding.set_service_url('https://api.us-south.natural-language-understanding.watson.cloud.ibm.com/instances/b89df6d6-7a5f-4da3-ae62-21655327f2fa')

    response = natural_language_understanding.analyze(
        text = text_value,
        features=Features(keywords=KeywordsOptions(sentiment=True,emotion=True,limit=2))).get_result()

    # print(json.dumps(response, indent=2))
    return response

response_recieved = keywords('hello world')
print(json.dumps(response_recieved, indent=2))