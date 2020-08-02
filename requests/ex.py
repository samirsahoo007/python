import requests

# get with auth token ###############################################################
url="https://mytestsite.hello.xyz.com/admin/info.json"
auth_token="xzfgfgfg4545sdfgfdsklyjhgj56456l;';;dfsdfk"

# Headers
# A header contains information about the client (type of browser), server, accepted response type, IP address, etc. 
# Headers can be customized for the source browser (user-agent) and content-type. They can be viewed using headers property as:
header_params = {"Accept": "application/json", "X-Auth-Token": auth_token}
r = requests.get(url, headers=header_params)
print(r.text)
print(r.headers)                         # print response headers 
print(r.headers['Content-Type'])         # output: application/json; charset=utf-8 

# downloading and saving an image ###############################################################
receive = requests.get('https://imgs.xkcd.com/comics/making_progress.png')
with open(r'C:\Users\Dell\Desktop\comics\image5.png','wb') as f:
    f.write(recieve.content)

# post request ###############################################################
pload = {'username':'olivia','password':'123'}
response = requests.post('https://httpbin.org/post',data = pload)

print(response.json())

if response.status_code == 200:
    print('Success!')
elif response.status_code == 404:
    print('Not Found.')

# With try catch ###############################################################
try: 
    response = requests.get(url,timeout=3) 
    response.raise_for_status()                 # Raise error in case of failure 
except requests.exceptions.HTTPError as httpErr: 
    print ("Http Error:",httpErr) 
except requests.exceptions.ConnectionError as connErr: 
    print ("Error Connecting:",connErr) 
except requests.exceptions.Timeout as timeOutErr: 
    print ("Timeout Error:",timeOutErr) 
except requests.exceptions.RequestException as reqErr: 
    print ("Something Else:",reqErr)

# Set timeout 
requests.get('https://github.com/', timeout=0.50)

# To disable redirection, set the allow_redirects parameter to False. By default it is set toTrue.
response = requests.get('http://github.com/', allow_redirects=True)
dest_url = response.url

# Cookies
# Cookies are small pieces of data stored on the client (browser) side and are often used to maintain a login session or to store user IDs.
# Both the client and server can send cookies. Use the cookies property to send and access cookies.
cookie = {'username':'Samir'} 
response = reqs.get('https://postman-echo.com/cookies/set',cookies = cookie)   # send cookie 
print(response.text)    # output: {"cookies":{"username":"Pavneet"}} 
print(response.cookies) # to access the cookies from server response

