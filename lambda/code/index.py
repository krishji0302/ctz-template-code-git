import json
from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

def lambda_handler(event, context):
    print("hello krishna, how are you today")
    print("current time is ", current_time)
    
    return {
        'statusCode': 200,
        'body': json.dumps('hello from Lambda--- krishna')
    }