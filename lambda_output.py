import json
import logging
import boto3
from boto3.dynamodb.conditions import Key, Attr

TABLENAME = "TOPICS"
client = boto3.client('dynamodb')
db = boto3.resource('dynamodb')
table = db.Table(TABLENAME)

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


def getAction(text):

    response = table.scan(
        FilterExpression=Attr('topic').eq(text)
    )

    print(response['Items'])

    if(len(response['Items']) > 0):
        answer = response['Items'][0]['answer']
    else:
        answer = "Lo siento no puedo entender que me dices, intanta nueva vez"

    return answer


def close(session_attributes, fulfillment_state, message):
    response = {
        'sessionAttributes': session_attributes,
        'dialogAction': {
            'type': 'Close',
            'fulfillmentState': fulfillment_state,
            'message': message
        }
    }

    return response


def delegate(session_attributes, slots):
    return {
        'sessionAttributes': session_attributes,
        'dialogAction': {
            'type': 'Delegate',
            'slots': slots
        }
    }


def get_answer(intent_request):

    question = intent_request['currentIntent']['slots']['lookup']

    resp = json.dumps({
        'QuestionType': 'Basic',
        'question': question
    })

    session_attributes = intent_request['sessionAttributes'] if intent_request['sessionAttributes'] is not None else {
    }

    session_attributes['currentQuestion'] = resp

    logger.debug('InvocationSource => {}'.format(
        intent_request['invocationSource']))

    if intent_request['invocationSource'] == 'FulfillmentCodeHook':
        # Validate any slots which have been specified.  If any are invalid, re-elicit for their value
        msg = getAction(question)

        logger.debug('Question ={}'.format(resp))

        return close(
            session_attributes,
            'Fulfilled',
            {
                'contentType': 'PlainText',
                'content': msg
            }
        )
    else:
        return delegate(session_attributes, intent_request['currentIntent']['slots'])

# --- Intents ---


def dispatch(intent_request):
    """
    Called when the user specifies an intent for this bot.
    """

    logger.debug('dispatch userId={}, intentName={}'.format(
        intent_request['userId'], intent_request['currentIntent']['name']))

    intent_name = intent_request['currentIntent']['name']

    # Dispatch to your bot's intent handlers
    if intent_name == 'Topic':
        return get_answer(intent_request)

    raise Exception('Intent with name ' + intent_name + ' not supported')


# --- Main handler ---

def lambda_handler(event, context):
    logger.debug('event.bot.name={}'.format(event['bot']['name']))

    return dispatch(event)
