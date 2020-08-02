import requests

# get with auth token
url="https://mytestsite.hello.xyz.com/admin/info.json"
auth_token="xzfgfgfg4545sdfgfdsklyjhgj56456l;';;dfsdfk"

header_params = {"Accept": "application/json", "X-Auth-Token": auth_token}
r = requests.get(url, headers=header_params)
print(r.text)

# downloading and saving an image 
receive = requests.get('https://imgs.xkcd.com/comics/making_progress.png')
with open(r'C:\Users\Dell\Desktop\comics\image5.png','wb') as f:
    f.write(recieve.content)

# post request
pload = {'username':'olivia','password':'123'}
response = requests.post('https://httpbin.org/post',data = pload)

print(response.json())

if response.status_code == 200:
    print('Success!')
elif response.status_code == 404:
    print('Not Found.')
