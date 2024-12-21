def lambda_handler(event, context):
    """
    AWS Lambda Function: Hello World
    """
    # Log the incoming event
    print("post call analysis")
    print("Event Received:", event)
    
    # Return a Hello World message
    return {
        "statusCode": 200,
        "body": "Hello, World from AWS Lambda!"
    }