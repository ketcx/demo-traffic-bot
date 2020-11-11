import logging
import boto3
from boto3.dynamodb.conditions import Key, Attr

TABLENAME_STOPWORDS = "STOPWORDS"
client = boto3.client('dynamodb')
db = boto3.resource('dynamodb')
table_stopwords = db.Table(TABLENAME_STOPWORDS)
columns_stopwords=["stopwords"]
    
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

def delegate(session_attributes, slots):
    return {
        'sessionAttributes': session_attributes,
        'dialogAction': {
            'type': 'Delegate',
            'slots': slots
        }
    }

def preprocess(text):
    
    response = table_stopwords.scan()
    
    text = text.lower()
    
    for x in response["Items"]:
        word = x['stopwords']
        text = text.replace(" "+word+" ", " ")
    
    text = text.strip()
    
    return text

def get_slots(intent_request):
    
    question = intent_request['inputTranscript']

    topics = preprocess(question)
    
    slots = {
      "lookup": topics,      
    };
    
    return slots

""" --- Functions that control the bot's behavior --- """


def generate_topic(intent_request):

    source = intent_request['invocationSource']

    if source == 'DialogCodeHook':
        
        output_session_attributes = intent_request['sessionAttributes'] if intent_request['sessionAttributes'] is not None else {}        

        return delegate(output_session_attributes, get_slots(intent_request))

""" --- Intents --- """


def dispatch(intent_request):
    """
    Called when the user specifies an intent for this bot.
    """

    logger.debug('dispatch userId={}, intentName={}'.format(intent_request['userId'], intent_request['currentIntent']['name']))

    intent_name = intent_request['currentIntent']['name']

    # Dispatch to your bot's intent handlers
    if intent_name == 'Topic':
        return generate_topic(intent_request)

    raise Exception('Intent with name ' + intent_name + ' not supported')


""" --- Main handler --- """


def lambda_handler(event, context):
    """
    Route the incoming request based on intent.
    The JSON body of the request is provided in the event slot.
    """
    return dispatch(event)
