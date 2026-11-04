import requests


def test_post_pet():
    response = requests.post("https://petstore.swagger.io/v2/pet", json={"name": "cat"})
    print(response.status_code)
    print(response.json())
    assert response.status_code == 200
    return response.json()["id"]


def test_get_pet(pet_id):
    response = requests.get(f"https://petstore.swagger.io/v2/pet/{pet_id}")
    print(response.status_code)
    print(response.json())
    assert response.status_code == 200


def test_put_pet(pet_id):
    response = requests.put("https://petstore.swagger.io/v2/pet", json={"id": pet_id, "name": "cat_doggie"})
    print(response.status_code)
    print(response.json())
    assert response.status_code == 200


def test_delete_pet(pet_id):
    response = requests.delete(f"https://petstore.swagger.io/v2/pet/{pet_id}")
    print(response.status_code)


new_pet_id = test_post_pet()
test_get_pet(new_pet_id)
test_put_pet(new_pet_id)
test_delete_pet(new_pet_id)
