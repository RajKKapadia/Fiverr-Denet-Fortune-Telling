from typing import List
import json


def formatResponse(messages: List[str], buttons: List[str] = [], images: List[str] = [], oc: List[dict] = []) -> dict:
    '''
    Formate the messages, buttons, and other things for Dialogflow

    Parameters:
        - messages(List(str)): messages to send
        - buttons(List(str)): buttons to send
        - images(List(str)): images to send
        - oc(List(dict)): Outputconetxt for Dialogflow, each object must have the name, and lifespanCount property
    '''

    fulfillment_text = json.dumps(
        {
            'messages': messages,
            'buttons': buttons,
            'images': images
        }
    )

    response_data = {
        'fulfillmentText': fulfillment_text
    }

    if len(oc) > 0:
        response_data['outputContexts'] = oc

    return response_data
