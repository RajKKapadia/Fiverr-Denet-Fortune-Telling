import os
import json


from google.cloud import dialogflow
from dotenv import load_dotenv
load_dotenv()


CREDENTIALS = json.loads(os.getenv('MY_CREDENTIALS'))
# os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.getenv('MY_CREDENTIALS')


# session_client = dialogflow.SessionsClient(**{'credentials': CREDENTIALS})
session_client = dialogflow.SessionsClient(**{
    'credentials': {
        'private_key': CREDENTIALS['private_key'],
        'client_email': CREDENTIALS['client_email']
    }
})


def detect_intent(session_id: str, query: str, language_code: str = 'en-US') -> dict:
    '''
    Detect intent of the user query and generate response.

    Parameters:
        - session_id(str): a unique session id for a user, must be same through out the conversations
        - query(str): query text from the user
        - language_code(str): language code of the input query, default en-US

    Returns:
        - dict
    '''

    session = session_client.session_path(
        CREDENTIALS['project_id'], session_id)
    text_input = dialogflow.TextInput(text=query, language_code=language_code)
    query_input = dialogflow.QueryInput(text=text_input)
    response = session_client.detect_intent(
        request={
            'session': session, 'query_input': query_input
        }
    )

    print(response)
    # print(response.query_result.intent.display_name)
    # print(response.query_result.intent_detection_confidence)
    # print(response.query_result.fulfillment_text)


detect_intent('abcdefg1234567', 'hi')
