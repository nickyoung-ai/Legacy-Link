import requests
BASE_URL = "http://127.0.0.1:8000"
login_data = {
    "username": "RoyalOne123",
    "password": "LegacyLink123!"
}
login_response = requests.post(f"{BASE_URL}/login", json=login_data)

if login_response.status_code != 200:
    print("Login failed", login_response.json())
    exit()

token = login_response.json().get("access_token")
headers = {
    "Authorization": f"Bearer {token}"
}
print("Login successful", login_response.json())

update_data = {
    "bio": "Updated bio",
    "location": "Ohio",
    "links": "https://example.com",
    "profile_picture_url": "https://example.com/picture.jpg"
}
update_response = requests.put(f"{BASE_URL}/profile", json=update_data, headers=headers)
print("Profile updated successfully", update_response.json())

username = login_data["username"]
get_response = requests.get(f"{BASE_URL}/profile/{username}", headers=headers)
print("Get profile:", get_response.json())
