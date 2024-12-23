from config import IAM_ROLES, CONFIG
# print(IAM_ROLES["ROLE1"])
config = CONFIG["Audio_To_Transcript"]["s3"]
region = config.get("region", "TEST")
print(CONFIG["Audio_To_Transcript"]["s3"])
