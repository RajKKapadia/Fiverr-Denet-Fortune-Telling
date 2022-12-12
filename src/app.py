from flask import Flask, request

from utils.utils import format_simple_response, process_request
from handlers.handlers import *
app = Flask(__name__)


@app.route('/')
def home():
    return 'OK', 200


@app.route('/dialogflow', methods=['POST'])
def dialogflow():

    data = request.get_json()

    action, _, _, _, _ = process_request(data)

    if action == 'confirmsDataPrivacy':
        response_data = confirms_data_privacy(data)
    elif action == 'userProvidesSelfie':
        response_data = user_provides_selfie(data)
    elif action == 'userProvidesName':
        response_data = user_provides_name(data)
    elif action == 'guestUserProvidesPassword':
        response_data = guest_user_provides_password(data)
    elif action == 'confirmsSendReport':
        response_data = confirms_send_report(data)
    elif action == 'registeredUserProvidesPassword':
        response_data = registered_user_provides_password(data)
    else:
        response_data = format_simple_response(
            [
                f'No handler for the action {action}.'
            ]
        )

    return response_data
