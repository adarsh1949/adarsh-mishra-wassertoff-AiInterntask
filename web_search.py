import requests

GOOGLE_API_KEY = "GOOGLE_API_KEY"  
SEARCH_ENGINE_ID = "SEARCH_ENGINE_ID"  

def google_search(query):
    url = f"https://www.googleapis.com/customsearch/v1?q={query}&key={GOOGLE_API_KEY}&cx={SEARCH_ENGINE_ID}"
    response = requests.get(url)
    data = response.json()

    if "items" in data:
        return data["items"][:3]  # Return top 3 results
    else:
        print("Error:", data)  # Print full API response for debugging
        return []

# Test the function
print(google_search("Latest AI trends"))
