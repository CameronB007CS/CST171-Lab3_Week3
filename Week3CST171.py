import requests
 
 
def get_first_five_post_titles():
    url = "https://jsonplaceholder.typicode.com/posts"
 
    response = requests.get(url)
    response.raise_for_status()  # Raises an error for bad status codes (4xx, 5xx)
 
    posts = response.json()
 
    print("First 5 Post Titles:")
    print("-" * 40)
    for i, post in enumerate(posts[:5], start=1):
        print(f"{i}. {post['title']}")
 
 
if __name__ == "__main__":
    get_first_five_post_titles()