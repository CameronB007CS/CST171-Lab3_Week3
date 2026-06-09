import requests


def fetch_endpoint(url, timeout=5):
    try:
        response = requests.get(url, timeout=timeout)

        if response.status_code == 200:
            print(f"  [200 OK] Successfully fetched: {url}")
            return response.json()

        elif response.status_code == 404:
            print(f"  [404 Not Found] Resource does not exist: {url}")

        elif response.status_code == 500:
            print(f"  [500 Server Error] Something went wrong on the server: {url}")

        else:
            print(f"  [{response.status_code}] Unexpected status code for: {url}")

    except requests.exceptions.Timeout:
        print(f"  [Timeout] Request timed out after {timeout}s: {url}")

    except requests.exceptions.ConnectionError:
        print(f"  [Connection Error] Could not connect to: {url}")

    except requests.exceptions.RequestException as e:
        print(f"  [Request Error] Something went wrong: {e}")

    return None


def main():
    endpoints = [
        "https://jsonplaceholder.typicode.com/posts/1",   # Valid - should succeed
        "https://jsonplaceholder.typicode.com/posts/999", # Invalid ID - returns a 404
        "https://jsonplaceholder.typicode.com/invalid",   # Bad endpoint - returns  a 404
        "https://httpstat.us/500",                        # Simulates 500 server error
        "https://httpstat.us/200?sleep=6000",             # Simulates timeout (6s delay)
    ]

    print("Testing API endpoints with error handling:")
    print("=" * 50)

    for url in endpoints:
        print(f"\nRequesting: {url}")
        data = fetch_endpoint(url, timeout=5)
        if data:
            print(f"  Data received: {str(data)[:80]}...")  # Print first 80 chars

    print("\n" + "=" * 50)
    print("All requests completed.")


if __name__ == "__main__":
    main()