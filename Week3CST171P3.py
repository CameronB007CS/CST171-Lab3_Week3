import requests


def create_post(user_id, title, body):
    url = "https://jsonplaceholder.typicode.com/posts"

    payload = {
        "userId": user_id,
        "title": title,
        "body": body
    }

    response = requests.post(url, json=payload)
    response.raise_for_status()

    new_post = response.json()

    print("Post created successfully!")
    print("=" * 50)
    print(f"  ID     : {new_post['id']}")
    print(f"  UserID : {new_post['userId']}")
    print(f"  Title  : {new_post['title']}")
    print(f"  Body   : {new_post['body']}")
    print("=" * 50)


if __name__ == "__main__":
    user_id = int(input("Enter your user ID: "))
    title = input("Enter post title: ")
    body = input("Enter post body: ")

    create_post(user_id, title, body)