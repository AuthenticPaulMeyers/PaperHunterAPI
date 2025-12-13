"""
API Endpoint Testing Script
Tests all HTTP methods for the user endpoints
"""
import requests
import json

BASE_URL = "http://127.0.0.1:8000/api/v1"

def print_response(name, response):
    """Pretty print response"""
    print(f"\n{'='*60}")
    print(f"Test: {name}")
    print(f"Status Code: {response.status_code}")
    try:
        print(f"Response: {json.dumps(response.json(), indent=2)}")
    except:
        print(f"Response: {response.text}")
    print(f"{'='*60}")

def test_endpoints():
    """Test all API endpoints"""
    
    import random
    suffix = random.randint(1000, 9999)
    test_user = {
        "username": f"testuser_{suffix}",
        "email": f"test_{suffix}@example.com",
        "password": "TestPass123!",
        "password_confirm": "TestPass123!",
        "full_name": "Test User"
    }
    
    token = None
    
    print("\n🚀 Starting API HTTP Method Tests...\n")
    
    # 1. Test Registration (POST)
    print("\n1️⃣ Testing POST /users/register/")
    try:
        response = requests.post(
            f"{BASE_URL}/users/register/",
            json=test_user
        )
        print_response("User Registration", response)
        if response.status_code == 201:
            token = response.json().get('token')
            print(f"✅ Registration successful! Token: {token[:20]}...")
        else:
            print(f"⚠️ Registration returned status {response.status_code}")
    except Exception as e:
        print(f"❌ Error: {e}")
    
    # 2. Test Login (POST)
    print("\n2️⃣ Testing POST /users/login/")
    try:
        response = requests.post(
            f"{BASE_URL}/users/login/",
            json={
                "username": test_user["username"],
                "password": test_user["password"]
            }
        )
        print_response("User Login", response)
        if response.status_code == 200:
            token = response.json().get('token')
            print(f"✅ Login successful! Token: {token[:20]}...")
        else:
            print(f"⚠️ Login returned status {response.status_code}")
    except Exception as e:
        print(f"❌ Error: {e}")
    
    if not token:
        print("\n❌ Cannot proceed without authentication token")
        return
    
    headers = {"Authorization": f"Token {token}"}
    
    # 3. Test Profile GET
    print("\n3️⃣ Testing GET /users/profile/")
    try:
        response = requests.get(
            f"{BASE_URL}/users/profile/",
            headers=headers
        )
        print_response("Get Profile", response)
        if response.status_code == 200:
            print("✅ Profile retrieved successfully!")
        else:
            print(f"⚠️ GET profile returned status {response.status_code}")
    except Exception as e:
        print(f"❌ Error: {e}")
    
    # 4. Test Profile PATCH
    print("\n4️⃣ Testing PATCH /users/profile/")
    try:
        response = requests.patch(
            f"{BASE_URL}/users/profile/",
            headers=headers,
            json={
                "full_name": "Updated Test User",
                "bio": "This is a test bio"
            }
        )
        print_response("Update Profile", response)
        if response.status_code == 200:
            print("✅ Profile updated successfully!")
        else:
            print(f"⚠️ PATCH profile returned status {response.status_code}")
    except Exception as e:
        print(f"❌ Error: {e}")
    
    # 5. Test Change Password (POST)
    print("\n5️⃣ Testing POST /users/change-password/")
    try:
        response = requests.post(
            f"{BASE_URL}/users/change-password/",
            headers=headers,
            json={
                "old_password": test_user["password"],
                "new_password": "NewPass123!",
                "new_password_confirm": "NewPass123!"
            }
        )
        print_response("Change Password", response)
        if response.status_code == 200:
            print("✅ Password changed successfully!")
        else:
            print(f"⚠️ Change password returned status {response.status_code}")
    except Exception as e:
        print(f"❌ Error: {e}")

    # 5.5 Re-login with new password to get new token
    print("\n🔄 Re-logging in with new password...")
    try:
        response = requests.post(
            f"{BASE_URL}/users/login/",
            json={
                "username": test_user["username"],
                "password": "NewPass123!"
            }
        )
        if response.status_code == 200:
            token = response.json().get('token')
            headers = {"Authorization": f"Token {token}"}
            print(f"✅ Re-login successful! New Token: {token[:20]}...")
        else:
            print(f"⚠️ Re-login failed: {response.status_code}")
    except Exception as e:
        print(f"❌ Re-login Error: {e}")
    
    # 6. Test Logout (POST)
    print("\n6️⃣ Testing POST /users/logout/")
    try:
        response = requests.post(
            f"{BASE_URL}/users/logout/",
            headers=headers
        )
        print_response("Logout", response)
        if response.status_code == 200:
            print("✅ Logout successful!")
        else:
            print(f"⚠️ Logout returned status {response.status_code}")
    except Exception as e:
        print(f"❌ Error: {e}")
    
    # 7. Test unauthorized access
    print("\n7️⃣ Testing Unauthorized Access (no token)")
    try:
        response = requests.get(f"{BASE_URL}/users/profile/")
        print_response("Unauthorized Profile Access", response)
        if response.status_code in [401, 403]:
            print("✅ Unauthorized access properly blocked!")
        else:
            print(f"⚠️ Expected 401, got {response.status_code}")
    except Exception as e:
        print(f"❌ Error: {e}")
    
    # 8. Test wrong HTTP methods
    print("\n8️⃣ Testing Wrong HTTP Method")
    try:
        response = requests.get(f"{BASE_URL}/users/register/")
        print(f"GET on /users/register/: Status {response.status_code}")
        if response.status_code == 405:
            print("✅ Method not allowed - correctly rejected!")
        else:
            print(f"⚠️ Expected 405, got {response.status_code}")
    except Exception as e:
        print(f"❌ Error: {e}")
    
    print("\n" + "="*60)
    print("✨ Testing Complete!")
    print("="*60)

if __name__ == "__main__":
    test_endpoints()
