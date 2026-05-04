import requests
url="https://jsonplaceholder.typicode.com/posts"
def get():
    
    response=requests.get(url)
    print(response.status_code)
def creat():
    
    data={
        "titl":"Zain Project",
        "body":"API test",
        "userId":1
    }
    response=requests.post(url,json=data)
    print(response.status_code)
    print(response.json())


def update():
    response = requests.put(url + "/1",json={
            "title": "updated proj",
            "body": "Tset 2",
            "userId": 2
        }
    )

    print("request-status:", response.status_code)
    print(response.json())

def delete():
    response = requests.delete(url + "/1")
    print("request-status:", response.status_code)
    print("Deleted")

def patch ():
    data = {
        "title": "First project"
    }

    response = requests.patch(url + "/1", json=data)
    print("request-status:", response.status_code)
    print(response.json())

get()
creat()
update()
delete()
patch()    

