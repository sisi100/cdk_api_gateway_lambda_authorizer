def hello(authorizer_context):
    return {
        "statusCode": 200,
        "body": f"Hello world! authorizer_context = {authorizer_context}",
    }
