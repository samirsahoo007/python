# Session Objects – Python requests
# Session object allows one to persist certain parameters across requests. 
# It also persists cookies across all requests made from the Session instance 
# and will use urllib3’s connection pooling. So if several requests are being 
# made to the same host, the underlying TCP connection will be reused, which 
# can result in a significant performance increase. A session object all the 
# methods as of requests.

import requests 
  
s = requests.Session()                              # create a session object 
  
s.get('https://httpbin.org/cookies/set/sessioncookie/123456789') 
  
r = s.get('https://httpbin.org/cookies') 
  
print(r.text)                                       # check if cookie is still set 
# '{"cookies": {"sessioncookie": "123456789"}}'

# One can check that cookie was still set when the request was made again.
# Sessions can also be used to provide default data to the request methods. This is done by providing data to the properties on a Session object:

s = requests.Session() 
s.auth = ('user', 'pass') 
s.headers.update({'x-test': 'true'}) 
  
s.get('https://httpbin.org / headers', headers ={'x-test2': 'true'}) 
  
print(s)

# how to clear all cookies in this variable?
s.cookies.clear()

