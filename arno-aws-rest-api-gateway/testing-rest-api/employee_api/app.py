import json
import logging
from aws_lambda_powertools.utilities.validation import validate

# CODE TEMPLATE OBTAINED FROM CODING TUTORIAL: JONATHAN DAVIES: YOUTUBE https://www.youtube.com/watch?v=4NY8nst45Rk
# https://gist.github.com/JonnyDavies/c8225e27334d036c9fa18cdccf4317e2
# CONVERTED NODE.JS CODE SYNTAX INTO PYTHON
# ENHANCED: Added AWS Lambda Powertools Validator for request validation

# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

EMPLOYEES = [
    {
        'name': 'bob',
        'employee_id': 121
    }
]

# Define validation schema for employee
employee_schema = {
    "type": "object",
    "required": ["name", "employee_id"],
    "properties": {
        "name": {"type": "string"},
        "employee_id": {"type": "integer"}
    }
}


def lambda_handler(event, context):
    try:
        # This is the gog to view full HTTP request in CloudWatch
        logger.info(event)
        
        result = ''
        
        if event['httpMethod'] == 'GET' and event['resource'] == '/employee':
            result = json.dumps(EMPLOYEES)
            
        elif event['httpMethod'] == 'POST' and event['resource'] == '/employee':
            # Parse the body and validate it
            request_body = json.loads(event['body'])
            validate(event=request_body, schema=employee_schema)
            
            EMPLOYEES.append(request_body)
            result = json.dumps(EMPLOYEES)
        
        response = {
            'statusCode': 200,
            'body': json.dumps({
                'message': result
            })
        }
        
    except Exception as err:
        logger.error(err)
        return {
            'statusCode': 400,
            'body': json.dumps({
                'message': str(err)
            })
        }
    
    return response