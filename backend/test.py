import requests

headers = {
    "Authorization": "YmF4OkJheHRpeW9yb3YyMTE3"
}

# params = {
#     "name": "CodeRed"
# }

# response = requests.post("http://192.168.0.106:5000/v1/organizations", headers=headers, params=params) # create category
# print(response.json())
# response = requests.get("http://192.168.0.106:5000/v1/organizations", headers=headers) # get category or categories
# print(response.json())
# response = requests.delete("http://192.168.0.106:5000/v1/organizations", headers=headers, params={"organization_id": 1}) # delete category
# print(response.json())

# params = {
#     "sec_role_id": 2,
#     "category_id": 1,
#     "username": "test",
#     "password": "secure_password",
#     "date_of_birth": "2000-02-21"
# }

# response = requests.get("http://192.168.0.106:5000/v1/users", headers=headers, params={"user_id": 1}) # get user or users
# print(response.json())
# response = requests.post("http://192.168.0.106:5000/v1/users", headers=headers, params=params) # create user
# print(response.json())
# response = requests.delete("http://192.168.0.106:5000/v1/users", params={"user_id": 2}) # delete user
# print(response.json())

# params = {
#     "name": "Ремонт"
# }

# response = requests.get("http://192.168.0.106:5000/v1/categories", headers=headers) # get category or categories
# print(response.json())
# response = requests.post("http://192.168.0.106:5000/v1/categories", headers=headers, params=params) # create category
# print(response.json())
# response = requests.delete("http://192.168.0.106:5000/v1/categories", headers=headers, params={"category_id": 1}) # delete category
# print(response.json())
