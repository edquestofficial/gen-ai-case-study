from config import IAM_ROLES, CONFIG
# print(IAM_ROLES["ROLE1"])
# config = CONFIG["Audio_To_Transcript"]["s3"]
# region = config.get("region", "TEST")
# print(CONFIG["Audio_To_Transcript"]["s3"])

# print(CONFIG["Audio_To_Transcript"]["test"]("Sunil"))

lambda_config = CONFIG["Audio_To_Transcript"]["lambda"]
LambdaFunctionConfigurations = lambda_config["LambdaFunctionConfigurations"]
AWS_ACCOUNT_ID = "Sunil_123"

LambdaFunctionConfigurations[0]["LambdaFunctionArn"] = LambdaFunctionConfigurations[0]["LambdaFunctionArn"].replace("AWS_ACCOUNT_ID", AWS_ACCOUNT_ID)
print(LambdaFunctionConfigurations)