import requests
url="https://jsonplaceholder.typicode.com/posts"

response=requests.get(url)
print(response.status_code)

data={
    "titl":"Zain Project",
    "body":"API test",
    "userId":1

}
response=requests.post(url,json=data)
print(response.status_code)
print(response.json())


response = requests.put("https://jsonplaceholder.typicode.com/posts/1", json={

    "title": "updated-first-post",
    "body": "new text",
    "userId": 2
}
)
print(response.status_code)
print(response.json())

response = requests.delete("https://jsonplaceholder.typicode.com/posts/1")
print(response.status_code)
print("Deleted")

data={"title":"First project"}
response=requests.patch(url="https://jsonplaceholder.typicode.com/posts/1",json=data)
print(response.status_code)
print(response.json())
print("Updated")