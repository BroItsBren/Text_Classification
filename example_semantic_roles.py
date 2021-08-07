import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, SemanticRolesOptions

authenticator = IAMAuthenticator('dvyhrBGP21qPssDUQ3AnRWvw0l3UdbyfmrWS_q64_I_q')
natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2021-08-01',
    authenticator=authenticator
)

natural_language_understanding.set_service_url('https://api.us-south.natural-language-understanding.watson.cloud.ibm.com/instances/513c3276-1ab3-4452-8af8-8ea8b4e31e51')

response = natural_language_understanding.analyze(
    text='A discipline that focuses on ensuring that only approved roles are able to create, read, update, or delete data – and only using appropriate and controlled methods. Data Governance programs often focus on supporting Access Management by aligning the requirements and constraints posed by  Governance, Risk Management, Compliance, Security, and Privacy efforts.',
    features=Features(semantic_roles=SemanticRolesOptions())).get_result()

print(json.dumps(response, indent=2))
