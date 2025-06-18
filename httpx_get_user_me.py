import httpx


login_payload = {
  "email": "alex2@ex.com",
  "password": "12345"
}

login_response = httpx.post("http://127.0.0.1:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()

me_headers = {"Authorization": f"Bearer {login_response_data['token']['accessToken']}"}
me_response = httpx.get("http://127.0.0.1:8000/api/v1/users/me", headers=me_headers)

print(me_response.status_code)
print(me_response.json())
