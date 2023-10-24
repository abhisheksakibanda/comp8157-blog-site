from http import HTTPStatus
from typing import List

import requests
from requests import Response

BASE_URL: str = "http://localhost:8000"
user_ids: List[str] = []
blog_ids: List[str] = []
comment_ids: List[str] = []


def populate_data() -> None:
    # POST APIs
    add_users()
    authenticate_users()
    add_blogs()
    add_comments()

    # GET APIs
    get_blogs()
    get_user_blogs()
    get_blog_comments()

    # PUT APIs
    update_blog()

    # DELETE APIs
    delete_blog_comment()
    delete_blogs()


def add_users() -> None:
    print("\nAdding users (POST /user/register)\n----------------------------------")

    test_users = [
        {
            "username": "sample_user",
            "email": "sampleuser@email.com",
            "password": "qwerty123456"
        },
        {
            "username": "test_user",
            "email": "testuser@email.com",
            "password": "qwertyuiop"
        }
    ]

    for user_payload in test_users:
        response: Response = requests.post(url=f"{BASE_URL}/user/register", json=user_payload)

        if not response.status_code == HTTPStatus.OK:
            print(f"Error registering user: {user_payload['username']}")
        else:
            print(f"\nStatus Code: {response.status_code}")
            print(f"User {user_payload['username']} registered successfully!\n")
            response_json = response.json()
            user_ids.append(response_json.pop("user_id"))

    print(f"User IDs: {user_ids}")


def authenticate_users():
    print("\nAuthenticate users (POST /user/authenticate)\n--------------------------------------------")

    test_users = [
        {
            "username": "sample_user",
            "password": "qwerty123456"
        },
        {
            "username": "test_user",
            "password": "qwertyuiop"
        }
    ]

    for user_payload in test_users:
        response: Response = requests.post(url=f"{BASE_URL}/user/authenticate", json=user_payload)

        if not response.status_code == HTTPStatus.OK:
            print(f"Error registering user: {user_payload['username']}")
        else:
            print(f"\nStatus Code: {response.status_code}")
            print(f"User {user_payload['username']} authenticated successfully!\n")
            print(f"Response:\n{response.json()}")


def add_blogs() -> None:
    print("\nAdding blogs (POST /blog/post)\n----------------------------")

    test_blogs = [
        {
            "title": "sample_title",
            "content": "sample_content",
            "author": user_ids[0],
        },
        {
            "title": "dummy_title",
            "content": "dummy_content",
            "author": user_ids[1],
            "categories": [
                "sample_category"
            ]
        }
    ]

    for blog_payload in test_blogs:
        response: Response = requests.post(url=f"{BASE_URL}/blog/post", json=blog_payload)

        if not response.status_code == HTTPStatus.OK:
            print(f"Error adding blog post: {blog_payload['title']}")
        else:
            print(f"\nStatus Code: {response.status_code}")
            print(f"Blog \"{blog_payload['title']}\" added successfully!\n")
            response_json = response.json()
            print("Response: \n", response_json)
            blog_ids.append(response_json.pop("id"))

    print(f"Blog IDs: {blog_ids}")


def get_blogs():
    print("\nGet All Blogs (GET /blog/all)\n-----------------------------")
    response: Response = requests.get(url=f"{BASE_URL}/blog/all")

    if not response.status_code == HTTPStatus.OK:
        print("Error fetching blogs")
    else:
        print("Response Code:", response.status_code)
        print(response.json())


def get_user_blogs():
    print("\nGet User Blogs (GET /blog/user/{user_id})\n-----------------------------------------")
    print(f"Blog IDs: {user_ids}")
    response: Response = requests.get(url=f"{BASE_URL}/blog/user/{user_ids[0]}")

    if not response.status_code == HTTPStatus.OK:
        print("Error fetching user blogs")
    else:
        print("Response Code:", response.status_code)
        print(response.json())


def update_blog():
    print("\nUpdate Blogs (PUT /blog/{blog_id})\n---------------------------------")
    response: Response = requests.put(url=f"{BASE_URL}/blog/{blog_ids[0]}", json={
        "title": "updated_title",
        "content": "updated_content",
        "categories": [
            "updated_category"
        ]
    })

    if not response.status_code == HTTPStatus.OK:
        print("Error updating blog")
    else:
        print("Response Code:", response.status_code)
        print(response.json())


def add_comments():
    print("\nAdding comments (POST /comment/post)\n-------------------------------------")

    test_comments = [
        {
            "name": "sample_comment_name",
            "text": "sample_text",
            "blog_id": blog_ids[0]
        },
        {
            "name": "dummy_comment",
            "text": "dummy_text",
            "blog_id": blog_ids[1]
        }
    ]

    for comment_payload in test_comments:
        response: Response = requests.post(url=f"{BASE_URL}/comment/post", json=comment_payload)

        if not response.status_code == HTTPStatus.OK:
            print(f"Error adding comment: {comment_payload.get('name')}")
            print(response.json())
        else:
            print(f"\nStatus Code: {response.status_code}")
            print(f"Comment \"{comment_payload.get('name')}\" added successfully!\n")
            comment_ids.append(response.json().pop("id"))


def get_blog_comments():
    print("\nGet Blog Comments (GET /blog/{blog_id}/comments)\n------------------------------------------------")
    response: Response = requests.get(url=f"{BASE_URL}/blog/{blog_ids[0]}/comments")

    print("Response Code:", response.status_code)
    print(response.json())


def delete_blog_comment():
    print("\nDelete Comments (DELETE /comment/{comment_id})\n---------------------------------------------")
    for comment_id in comment_ids:
        response: Response = requests.delete(url=f"{BASE_URL}/comment/{comment_id}")

        print("\nResponse Code:", response.status_code)
        print("Deleted following comment:\n", response.json())


def delete_blogs():
    for blog_id in blog_ids:
        print("\nDelete Blogs (DELETE /blog/{blog_id})\n-----------------------------------------")
        response: Response = requests.delete(url=f"{BASE_URL}/blog/{blog_id}")

        print("\nResponse Code:", response.status_code)
        print("Deleted following blog:\n", response.json())


if __name__ == '__main__':
    populate_data()
