import requests
from requests.auth import HTTPBasicAuth

login_url = 'http://127.0.0.1:8000/login/'

session = requests.Session()
#print("requests.session =", session)

session.get(login_url)
#print(session.get(login_url))   

csrf_token = session.cookies.get('csrftoken', '')
#print("csrf_token =", csrf_token)

login_data = {
    'username': 'rohy',
    'password': '1234',
    'csrfmiddlewaretoken': csrf_token
}

headers = {
    'Referer': login_url
}

response = session.post(login_url, data=login_data, headers=headers)

print(f"Status Code: {response.status_code}")
print(f"Response: {response.text}")

# Now you can access protected pages
#protected_response = session.get('http://127.0.0.1:8000')
#print(protected_response.text)


#print(response.headers)
#print(response.status_code)
#print(response.text)

