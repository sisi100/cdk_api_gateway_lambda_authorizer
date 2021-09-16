def authorizer(token, resources):
    if (length := len(token)) <= 1:
        raise Exception("Unauthorized")
    return {
        "principalId": "hogehoge_principal_id",
        "policyDocument": {
            "Version": "2012-10-17",
            "Statement": [{"Action": "execute-api:Invoke", "Effect": "Allow", "Resource": resources}],
        },
        "context": {"hogehoge_token_length": length},
    }
