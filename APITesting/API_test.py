import requests


class TestAPI:

    BASE_URL = "https://reqres.in/api"

    def test_get_single_user(self):
        obj=TestAPI()
        response = requests.get(f"{obj.BASE_URL}/users/2")
        assert response.status_code == 200
        jsonData = response.json()
        print("id is -->",jsonData['data']['id'])
        assert jsonData["data"]["id"] == 2
        assert jsonData["data"]["email"] == "janet.weaver@reqres.in"

    def test_create_user(self):
        obj = TestAPI()
        payload = {
            "name": "Rahul",
            "job": "Manager"
        }

        response = requests.post(f"{obj.BASE_URL}/users", json=payload)
        assert response.status_code == 201
        data = response.json()
        print("Response Data ",data)
        assert data["name"] == payload["name"]
        assert data["job"] == payload["job"]

    def test_update_user(self):
        obj = TestAPI()
        payload = {
            "name": "neo",
            "job": "zion resident"
        }
        response = requests.put(f"{obj.BASE_URL}/users/2", json=payload)
        assert response.status_code == 200
        data = response.json()
        assert data["name"] == payload["name"]
        assert data["job"] == payload["job"]

    def test_delete_user(self):
        obj = TestAPI()
        response = requests.delete(f"{obj.BASE_URL}/users/2")
        assert response.status_code == 204

    def test_user_not_found(self):
        obj = TestAPI()
        response = requests.get(f"{obj.BASE_URL}/users/23")
        assert response.status_code == 404

