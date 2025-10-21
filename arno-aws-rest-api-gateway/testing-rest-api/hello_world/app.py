import json
import logging


# CODE TEMPLATE OBTAINED FROM CODING TUTORIAL: JONATHAN DAVIES: YOUTUBE https://www.youtube.com/watch?v=4NY8nst45Rk
# https://gist.github.com/JonnyDavies/c8225e27334d036c9fa18cdccf4317e2
# CONVERTED NODE.JS CODE SYNTAX INTO PYTHON


# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

EMPLOYEES = [
    {
        'name': 'bob',
        'employee_id': 121
    }
]

def lambda_handler(event, context):
    try:
        # Log to view full HTTP request in CloudWatch
        logger.info(event)
        
        result = ''
        
        if event['httpMethod'] == 'GET' and event['resource'] == '/employee':
            result = json.dumps(EMPLOYEES)
        elif event['httpMethod'] == 'POST' and event['resource'] == '/employee':
            EMPLOYEES.append(json.loads(event['body']))
            result = json.dumps(EMPLOYEES)
        
        response = {
            'statusCode': 200,
            'body': json.dumps({
                'message': result
            })
        }
        
    except Exception as err:
        logger.error(err)
        return err
    
    return response