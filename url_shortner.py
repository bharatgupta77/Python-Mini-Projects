import bitly_api

# bitly access token - please add your own api access token below
access_Token = ""

# establish a connection with bitly_api
connection = bitly_api.Connection(access_token=access_Token)

# take the url from user
url = input("Enter the url you wish to shorten: ").strip()

#to shorten the url, using shorten method
shorten_url = connection.shorten(url)

# print shorten url
print(shorten_url.get('url'))
