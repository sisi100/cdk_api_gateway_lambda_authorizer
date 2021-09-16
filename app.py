from aws_cdk import core as cdk

from cdk_api_gateway_lambda_authorizer.cdk_api_gateway_lambda_authorizer_stack import CdkApiGatewayLambdaAuthorizerStack

app = cdk.App()
CdkApiGatewayLambdaAuthorizerStack(app, "CdkApiGatewayLambdaAuthorizerStack")
app.synth()
