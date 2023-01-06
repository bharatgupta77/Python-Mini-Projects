import random as r

"""
randint() is an inbuilt function of the random module in Python3. The random module gives access to various useful functions and one of them being able to generate random numbers, which is randint().
"""

# function for otp generation


def otp_generation():
    otp_l = ""
    # length of otp is 6
    for i in range(6):
        otp_l += str(r.randint(0, 9))
    return otp_l


otp = otp_generation()
print("Your one time password is : "+otp)
