import requests


HEADERS = {"User-Agent": "CST171-Reddit-Client/1.0"}


def get_top_posts(subreddit, num_posts):
    url = f"https://www.reddit.com/r/{subreddit}/top.json"
    params = {"limit": num_posts, "t": "day"}

    try:
        response = requests.get(url, headers=HEADERS, params=params, timeout=5)

        if response.status_code == 404:
            print(f"  [404 Not Found] Subreddit 'r/{subreddit}' does not exist.")
            return

        elif response.status_code == 403:
            print(f"  [403 Forbidden] Subreddit 'r/{subreddit}' is private.")
            return

        response.raise_for_status()

        data = response.json()
        posts = data["data"]["children"]

        if not posts:
            print(f"  No posts found in r/{subreddit}.")
            return

        print(f"\nTop {num_posts} posts from r/{subreddit}:")
        print("=" * 60)

        for i, post in enumerate(posts, start=1):
            p = post["data"]
            title = p["title"]
            score = p["score"]
            url   = f"https://reddit.com{p['permalink']}"

            print(f"\n#{i} - {title}")
            print(f"  Score : {score} upvotes")
            print(f"  URL   : {url}")
            print("-" * 60)

    except requests.exceptions.Timeout:
        print("  [Timeout] Request timed out. Try again later.")

    except requests.exceptions.ConnectionError:
        print("  [Connection Error] Could not connect. Check your internet.")

    except requests.exceptions.RequestException as e:
        print(f"  [Error] Something went wrong: {e}")


if __name__ == "__main__":
    subreddit = input("Enter subreddit name (without r/): ")
    num_posts = int(input("How many posts would you like to see? "))
    get_top_posts(subreddit, num_posts)