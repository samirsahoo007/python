# When you keep peeling back the onion, Session.request creates an instance of the PreparedRequest object. You can construct these objects by hand, typically when you have a specific binary payload to send and set of headers.

import requests

with requests.Session() as sess:
  req = requests.Request('post', 'https://my-api.service.com/api/v1/example')
  prepped = session.prepare_request(req)
  prepped.body = my_data
  response = session.send(prepped)

