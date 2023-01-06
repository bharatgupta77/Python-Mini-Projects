import random as r

"""
randint() is an inbuilt function of the random module in Python3. The random module gives access to various useful functions and one of them being able to generate random numbers, which is randint().
"""

# function for otp generation. OTP of length n will be generated.


def otp_generation(n):
    otp_l = ""
    for i in range(n):
        otp_l += str(r.randint(0, 9))
    return otp_l


print("Enter the length of OTP you want :")
n = int(input())

otp = otp_generation(n)
print("Your one time password is : "+otp)
