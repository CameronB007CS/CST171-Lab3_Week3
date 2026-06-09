import requests
 
 
def get_posts_by_user(user_id):
    url = "https://jsonplaceholder.typicode.com/posts"
    params = {"userId": user_id}
 
    response = requests.get(url, params=params)
    response.raise_for_status()
 
    posts = response.json()
 
    if not posts:
        print(f"No posts found for user ID {user_id}.")
        return
 
    print(f"Posts by User ID {user_id}:")
    print("=" * 50)
    for i, post in enumerate(posts, start=1):
        print(f"\nPost {i}:")
        print(f"  Title : {post['title']}")
        print(f"  Body  : {post['body']}")
        print("-" * 50)
 
 
if __name__ == "__main__":
    user_id = int(input("Enter a user ID (1-10): "))
    get_posts_by_user(user_id)
 