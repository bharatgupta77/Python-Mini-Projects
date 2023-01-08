

"""
function email slicer is used to separate the username and domain name of an email address.
"""


def email_slicer(email):
    # strip is used to remove leading and trailing spaces from the string
    email = email.strip()
    seperator_index = email.index("@")
    username = email[:seperator_index]
    domain_name = email[seperator_index+1:]
    return username, domain_name


email = input("Enter your email : ")
username, domain_name = email_slicer(email)

print("Your username is : "+username)
print("Your domain is : "+domain_name)
