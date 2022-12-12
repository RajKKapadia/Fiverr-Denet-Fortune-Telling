from flask import Flask, request

from utils.utils import formatResponse

app = Flask(__name__)

@app.route('/')
def home():
    return 'OK', 200

@app.route('/dialogflow', methods=['POST'])
def dialogflow():

    data = request.get_json();

    print(data)

    return formatResponse(
        [
            'From the webhook'
        ]
    )