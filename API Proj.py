import requests
url = "https://jsonplaceholder.typicode.com/posts"

def api_get():
    try:
        response = requests.get(url)
        print("Status:", response.status_code)
        print(response.json())
    except Exception as e:
        print("Error:", e)

def create():
    try:
        data = {
            "title": "Zain Project",
            "body": "API test",
            "userId": 1
        }
        response = requests.post(url, json=data)
        print("Status:", response.status_code)
        print(response.json())

    except Exception as e:
        print("Error:", e)

def update():
    try:
        response = requests.put(url + "/1", json={
            "title": "updated proj",
            "body": "Test",  
            "userId": 2
        })

        print("Status:", response.status_code)
        print(response.json())

    except Exception as e:
        print("Error:", e)

def delete():
    try:
        response = requests.delete(url + "/1")
        print("Status:", response.status_code)

        if response.status_code == 200:
            print("Deleted")
        else:
            print("Delete failed")

    except Exception as e:
        print("Error:", e)

def patch():
    try:
        data = {
            "title": "First project"
        }

        response = requests.patch(url + "/1", json=data)
        print("Status:", response.status_code)
        print(response.json())

    except Exception as e:
        print("Error:", e)


api_get()
create()
update()
delete()
patch()
