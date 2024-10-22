Searchry: Google Custom Search Scraper

Searchry is a versatile Python tool that allows you to perform Google Custom Searches for any query and save the results to an Excel file. Whether you're looking for research internships, job listings, or general information, Searchry helps you get relevant results quickly and efficiently.
Features

    Fetches search results using Google Custom Search API.
    Allows flexible querying based on user-defined search terms.
    Extracts the title, link, and snippet for each result.
    Saves the results to an Excel file (.xlsx) for easy review.

Prerequisites

Make sure you have the following installed:

    Python 3.x
    Required Python libraries: requests, pandas, and openpyxl

You can install the required libraries using:

bash

pip install requests pandas openpyxl

Setup

    Google Custom Search API Key & Engine ID:
        Obtain an API key by creating a project on the Google Cloud Console.
        Create a Custom Search Engine and note the Engine ID.
        Replace API_KEY and CX in the script with your API key and Custom Search Engine ID.

    Clone the Repository:

    bash

git clone https://github.com/yourusername/searchry.git
cd searchry

Configure API Credentials: Edit the script file (searchry.py) and replace the following:

python

    API_KEY = 'Your-Api-Key'
    CX = 'your-engine-id'

Usage

Run the script using:

bash

python searchry.py

The script will:

    Fetch up to 100 search results, 10 at a time.
    Save the results to search_results.xlsx.

Note:

The script uses a delay of 1 second between each request to respect API rate limits.
Output

The script will create an Excel file named search_results.xlsx with the following columns:

    Title: Title of the search result.
    Link: URL of the search result.
    Snippet: A short description of the content.

Limitations

    The free tier of Google Custom Search API allows up to 100 requests per day, and each request can return a maximum of 10 results.
    Ensure you do not exceed your quota limit by monitoring usage on the Google Cloud Console.

Error Handling

The script includes basic error handling:

    If an HTTP error occurs (e.g., due to invalid API key), it will display an error message and stop the script.
    For other general errors, a message will be printed, and the script will exit gracefully.

Contributing

Feel free to contribute to this project by submitting issues or pull requests. Make sure to follow the coding standards and include relevant tests.
License
