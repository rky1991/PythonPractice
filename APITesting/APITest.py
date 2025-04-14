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
