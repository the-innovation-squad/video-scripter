import requests
from config import Config
cfg = Config()

def search_footage(tag):
    headers = {
        "Content-Type": "application/json",
        "Authorization": cfg.pexels_api_key
    }
    url=f"https://api.pexels.com/videos/search?query={tag}&per_page=1"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        results = response.json()
        videos = results.get("videos")
        if videos:
            return videos[0].get("video_files")[0].get("link")
        return None
    else:
        print("Request failed with status code:", response.status_code)
        print("Response content:", response.content)
        raise Exception("Pexels API search failed: " + response.content)

def search(tags):
    tags_array = tags.split(",")
    for tag in tags_array:
        result = search_footage(tag.strip())
        if result is not None:
            return result
    raise Exception("No results found for tags: " + str(tags))