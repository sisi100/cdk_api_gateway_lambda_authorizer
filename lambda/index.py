from authorizer import authorizer
from hello import hello


def authorizer_handler(event, context):
    token = event["authorizationToken"]
    resources = [event["methodArn"]]
    return authorizer(token, resources)


def hello_handler(event, context):
    authorizer_context = event["requestContext"]["authorizer"]
    return hello(authorizer_context)
