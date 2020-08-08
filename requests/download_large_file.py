import six
import requests

chunk_size = 8096
bytes_transferred = 0
response = requests.get('https://website.com/large_file', stream=True)

with open('my_file.zip', 'wb') as file_handle:
    for chunk in response.iter_content(chunk_size):
        file_handle.write(six.b(chunk))
        bytes_transferred += len(chunk)
        print("Downloaded {0} bytes".format(bytes_transferred))

