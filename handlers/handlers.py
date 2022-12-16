from utils.utils import process_output_context, process_request, format_simple_response


def confirms_data_privacy(data: dict) -> dict:
    '''
    Handler for confirmsDataPrivacy action for Dialogflow

    Parameters:
        - data(dict): incoming data from Dialogflow

    Retunrs:
        - dict: response for Dialogflow
    '''

    _, output_contexts, _, _, session = process_request(data)

    parameters = process_output_context(output_contexts)

    if 'person' in parameters.keys():

        oc = [
            {
                'name': f'{session}/contexts/await-image',
                'lifespanCount': 1
            }
        ]

        name = parameters['person']['name']

        return format_simple_response(
            message=f'Thank you {name.capitalize()} for agreeing to our Terms of use. now I want you do upload the cup image.',
            oc=oc
        )


def user_provides_selfie(data: dict) -> dict:
    '''
    Handler for userProvidesSelfie action for Dialogflow

    Parameters:
        - data(dict): incoming data from Dialogflow

    Retunrs:
        - dict: response for Dialogflow
    '''

    _, output_contexts, _, _, session = process_request(data)

    parameters = process_output_context(output_contexts)

    '''
    TODO
    if registered don't ask for relationship status
    '''

    if 'person' in parameters.keys():

        oc = [
            {
                'name': f'{session}/contexts/await-relation-status',
                'lifespanCount': 1
            }
        ]

        name = parameters['person']['name']

        return format_simple_response(
            message=f'Ok {name.capitalize()}. One more question left: What is your relationship status?',
            oc=oc
        )


def user_provides_name(data: dict) -> dict:
    '''
    Handler for userProvidesName action for Dialogflow

    Parameters:
        - data(dict): incoming data from Dialogflow

    Retunrs:
        - dict: response for Dialogflow
    '''

    _, output_contexts, _, _, session = process_request(data)

    parameters = process_output_context(output_contexts)

    if 'person' in parameters.keys():

        oc = [
            {
                'name': f'{session}/contexts/await-relation-status',
                'lifespanCount': 1
            }
        ]

        name = parameters['person']['name']

        return format_simple_response(
            message=f'Good to meet you {name.capitalize()}, Do you agree the Terms of use and GDPR?',
            oc=oc
        )


def guest_user_provides_password(data: dict) -> dict:
    '''
    Handler for guestUserProvidesPassword action for Dialogflow

    Parameters:
        - data(dict): incoming data from Dialogflow

    Retunrs:
        - dict: response for Dialogflow
    '''

    _, output_contexts, _, _, _ = process_request(data)

    parameters = process_output_context(output_contexts)

    '''
    TODO:
    create new user
    '''

    if 'person' in parameters.keys():

        name = parameters['person']['name']

        return format_simple_response(
            message=f'Great, you are now my resgitred user {name.capitalize()}. I hope you enjoyed yourself.'
        )


def confirms_send_report(data: dict) -> dict:
    '''
    Handler for confirmsSendReport action for Dialogflow

    Parameters:
        - data(dict): incoming data from Dialogflow

    Retunrs:
        - dict: response for Dialogflow
    '''

    _, output_contexts, _, _, session = process_request(data)

    parameters = process_output_context(output_contexts)

    name = parameters['person']['name']

    if 'user-status' in parameters.keys():

        '''
        TODO:
        registered user so send the report directly
        '''

        return format_simple_response(
            message=f'Ok. Hope to see you soon {name.capitalize()}. Bye for now. [Exits]'
        )
    else:

        oc = [
            {
                'name': f'{session}/contexts/await-guest-email',
                'lifespanCount': 1
            }
        ]

        return format_simple_response(
            message=f'Okay {name.capitalize()}, please provide your valid email address to receive a copy.',
            oc=oc
        )


def registered_user_provides_password(data: dict) -> dict:
    '''
    Handler for registeredUserProvidesPassword action for Dialogflow

    Parameters:
        - data(dict): incoming data from Dialogflow

    Retunrs:
        - dict: response for Dialogflow
    '''

    '''
    TODO
    [] check registration...
    '''

    

    return format_simple_response(
        message='Good to see you [User name]. So for this reading session just send me your cup image.'
    )
