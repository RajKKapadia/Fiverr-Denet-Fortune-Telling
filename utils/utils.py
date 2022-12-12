from typing import List
import json

from flask import request


def format_complex_response(messages: List[str], buttons: List[str] = [], images: List[str] = [], oc: List[dict] = []) -> dict:
    '''
    Formate the messages, buttons, and other things for Dialogflow

    Parameters:
        - messages(List[str]): messages to send
        - buttons(List[str]): buttons to send
        - images(List[str]): images to send
        - oc(List[dict]): Outputconetxt for Dialogflow, each object must have the name, and lifespanCount property
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


def format_simple_response(message: str, oc: List[dict] = []) -> dict:
    '''
    Formate the messages, buttons, and other things for Dialogflow

    Parameters:
        - messages(str): message to send
        - oc(List(dict)): Outputconetxt for Dialogflow, each object must have the name, and lifespanCount property
    '''

    response_data = {
        'fulfillmentText': message
    }

    if len(oc) > 0:
        response_data['outputContexts'] = oc

    return response_data


def process_request(data: dict) -> tuple:
    '''
    Process the incoming request on the server for Dialogflow

    Parameters:
        - data(dict): flask request object

    Returns:
        - tuple of things action, output_contexts, intent_name, query, session
    '''
    
    action = data['queryResult']['action']
    output_contexts = data['queryResult']['outputContexts']
    intent_name = data['queryResult']['intent']['displayName']
    query = data['queryResult']['queryText']
    
    session = ''
    if 'session' in data.keys():
        session = data['session']

    return action, output_contexts, intent_name, query, session


def process_output_context(output_contexts: List[dict]) -> dict:
    '''
    Process the output context of Dialogflow, get parameters from the session

    Parameters:
        - output_contexts(List[dict]): incoming list of output contexts

    Returns:
        - dict: 
    '''

    parameters = {}

    for oc in output_contexts:

        if 'session-vars' in oc['name']:
            parameters = oc['parameters']

    return parameters
