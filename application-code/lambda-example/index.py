import json

def lambda_handler(event, context):
    # Log the received event
    print(f"Received event: {json.dumps(event)}")

    # Create a response
    response = {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Hello, World!",
        }),
    }

    return response
