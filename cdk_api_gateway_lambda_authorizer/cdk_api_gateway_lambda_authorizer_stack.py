from aws_cdk import core as cdk
from aws_cdk.aws_apigateway import IdentitySource, LambdaIntegration, RestApi, TokenAuthorizer
from aws_cdk.aws_lambda import Runtime
from aws_cdk.aws_lambda_python import PythonFunction

APP_NAME = "CdkApiGatewayLambdaAuthorizer"


class CdkApiGatewayLambdaAuthorizerStack(cdk.Stack):
    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        common_lambda_param = {"entry": "lambda", "runtime": Runtime.PYTHON_3_8}
        auth_lambda = PythonFunction(self, f"{APP_NAME}AuthLambda", handler="authorizer_handler", **common_lambda_param)
        hello_lambda = PythonFunction(self, f"{APP_NAME}HelloLambda", handler="hello_handler", **common_lambda_param)

        api = RestApi(self, f"{APP_NAME}Api")
        auth = TokenAuthorizer(
            self, "hoge_authorizer", identity_source=IdentitySource.header("HogeAuthorization"), handler=auth_lambda
        )
        api.root.add_method("GET", LambdaIntegration(hello_lambda), authorizer=auth)
