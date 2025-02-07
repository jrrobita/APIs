# tutorial from datacamp:
# https://www.datacamp.com/tutorial/making-http-requests-in-python


#concept: to get data back, first you have to requst in -> requests

#the basics

#a 'get' request

import requests

# The API endpoint
url = "https://jsonplaceholder.typicode.com/posts/1"

# A GET request to the API
response = requests.get(url)

# Print the response
print(response.json())


# a'post' request

# Data to be sent
data = {
    "userID": 1,
    "title": "Making a POST request",
    "body": "This is the data we created."
}

# A POST request to the API
response = requests.post(url, json=data)

# Print the response
print(response.json())



#To add more context, REST APIs expose a set of public URLs 
# that may be requested by client applications to access the 
# resources of the web service. 

# The public URLs exposed by the REST API are known as “endpoints.”


#specify parameters to get different response objects back

# The API endpoint
#note: goinging to a higher level in the https address
url = "https://jsonplaceholder.typicode.com/posts/"

# Adding a payload
# basically the values for which the select records for specified vars
payload = {"id": [1, 2, 3], "userId":1}

# A get request to the API
response = requests.get(url, params=payload)

# Print the response
response_json = response.json()

#returns a list (of dictionaries) since there are multiple responses

#print each ele in that list
for i in response_json:
    print(i, "\n")


## authentication

# There are several instances where a REST API may require authentication 
# before access is granted to specific endpoints – especially when you’re 
# dealing with sensitive data. 

# For example, if you want to create integrations, retrieve data, and automate 
# your workflows on GitHub, you can do so with the GitHub REST API. However, 
# there are many operations on the GitHub REST API that require authentication, 
# such as retrieving public and private information about authenticated users. 