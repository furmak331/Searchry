import requests
import pandas as pd
import math
import time

# Import datetime for dynamic date calculations (if needed in the future)
from datetime import datetime, timedelta

# **IMPORTANT:** Ensure you keep your API keys secure. Avoid sharing them publicly.
API_KEY = 'Your-Api-Key'  # Ensure this is your correct API key
CX = 'your-engine-id'  # Ensure this is your correct Custom Search Engine ID

# Define the search query
QUERY = 'winter research intern india'

# Number of results per request (max 10 for Google API)
RESULTS_PER_PAGE = 10

# Maximum number of results you want (Google API allows up to 100 for free)
MAX_RESULTS = 100

# Initialize list to store results
results = []

def google_search(query, api_key, cx, start_index, date_restrict):
    url = 'https://www.googleapis.com/customsearch/v1'
    params = {
        'q': query,
        'key': api_key,
        'cx': cx,
        'start': start_index,
        'num': RESULTS_PER_PAGE,
        'dateRestrict': date_restrict  # Add date restriction parameter
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()

def extract_items(json_response):
    items = json_response.get('items', [])
    extracted = []
    for item in items:
        title = item.get('title')
        link = item.get('link')
        snippet = item.get('snippet')
        extracted.append({
            'Title': title,
            'Link': link,
            'Snippet': snippet
        })
    return extracted

def main():
    total_pages = math.ceil(MAX_RESULTS / RESULTS_PER_PAGE)
    # Set dateRestrict to past 3 weeks
    date_restrict = 'w3'  # Options: 'w2' for 2 weeks, 'w3' for 3 weeks, etc.
    
    for page in range(total_pages):
        start_index = page * RESULTS_PER_PAGE + 1
        try:
            print(f"Fetching results {start_index} to {start_index + RESULTS_PER_PAGE -1}...")
            json_response = google_search(QUERY, API_KEY, CX, start_index, date_restrict)
            items = extract_items(json_response)
            results.extend(items)
            # Respectful delay to avoid hitting rate limits
            time.sleep(1)
        except requests.exceptions.HTTPError as err:
            print(f"HTTP Error: {err}")
            break
        except Exception as e:
            print(f"An error occurred: {e}")
            break

    if not results:
        print("No results found for the specified query and date range.")
        return

    # Create a DataFrame
    df = pd.DataFrame(results)

    # Save to Excel
    output_file = 'research_internships_recent.xlsx'
    df.to_excel(output_file, index=False)
    print(f"Data saved to {output_file}")

if __name__ == '__main__':
    main()
