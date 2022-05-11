import onetimepass as otp

secret = 'bjs3obz3yphrvgq7olvlukc4uttldysh'
token = otp.get_totp(secret)
print(token)