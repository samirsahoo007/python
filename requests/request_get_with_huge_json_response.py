import requests
import time
import json

no_of_days=40
system_name="xyz.mycomp.network"
end_time = int(time.time())
no_of_days_in_secs = no_of_days * 24 * 60 * 60
start_time = end_time - no_of_days_in_secs
url = "https://xyz.mno.com/api/1.0/myapi/jobruns/list"

params = {"size": 8921}

payload = {
    "operator": "and",
    "filters": [
        {
            "operator": "ge",
            "field": "created_date",
            "value": start_time
        },
        {
            "operator": "le",
            "field": "created_date",
            "value": end_time
        },
        {
            "operator": "eq",
            "field": "system_name",
            "value": system_name
        },
        {
            "operator": "in",
            "field": "status",
            "value": [
                "FAILED",
                "PASSED"
            ]
        }
    ]
}

with requests.post(url, data=json.dumps(payload), params=params, verify=False, stream=True) as resp:
    data=""
    for chunk in resp.iter_content(chunk_size=4096, decode_unicode=False):  # 4K at a time
        chunk = chunk.decode('utf-8')
        data += chunk
    print(data)

print(type(data))
jobs_ran=json.loads(data)
print(jobs_ran)

