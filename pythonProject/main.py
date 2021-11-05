import requests as req
host='localhost'
port=8000
body={}
params={
    "page":2
}

response=req.get('https://reqres.in/api/users',data=body,params=params,timeout=3)

print(response.json())
