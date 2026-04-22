import requests

def get_data(query):
    url = f"http://127.0.0.1:6878/search?query={query}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        search_results = data.get("result", {}).get("results", [])
        
        extracted_data = []
        
        for entry in search_results:
            for item in entry.get("items", []):
                name = item.get("name")
                infohash = item.get("infohash")
                dd_link = f"http://127.0.0.1:6878/ace/getstream?id={infohash}&hlc=1&transcode_audio=0&transcode_mp3=0&transcode_ac3=0&preferred_audio_language=eng"
                extracted_data.append({
                    "name": name,
                    "link": dd_link
                })
                
        return extracted_data

    except Exception as e:
        return f"Error: {e}"

def input_search():
    query = input("Enter search query: ")
    results = get_data(query)
    if results:
        for res in results:
            print(f"Stream: {res['name']}")
            print(f"Link:   {res['link']}\n")
    else:
        print("No streams found.")