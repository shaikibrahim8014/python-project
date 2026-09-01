# OTP generator
import random
import string

OTP_LENGTH = 3
otp = random.choice(string.digits)
for _ in range(OTP_LENGTH ):
    otp += random.choice(string.digits)
print("Your OTP is:", otp)
