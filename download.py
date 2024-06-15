import requests
import os
# Define the URL of the CSV file


def download(url, filename):
    if os.path.exists(filename):
        print('file already exists.')
        return False

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
    }

    try:
        response = requests.get(url, headers=headers)
        # Raise an exception for unsuccessful requests (e.g., 403 Forbidden)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print("Error downloading file:", e)
        return False

    with open(filename, "wb") as f:
        f.write(response.content)
    print(f"downloaded successfully to: {filename}")

    return True