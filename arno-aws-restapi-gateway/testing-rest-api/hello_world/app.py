import json
import logging

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
        # Log to view full Http request in Cloudwatch
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
        return str(err)
    
    return response