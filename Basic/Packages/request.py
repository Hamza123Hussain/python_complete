# Import necessary modules
import requests  # Module to send HTTP requests in Python
import json      # Module to handle JSON data

# Ask the user to input the artist's name
name = input('Enter Artist Name: ')

# Send a GET request to the iTunes API using the artist's name entered by the user
# 'entity=song' limits the search results to songs
# 'limit=10' restricts the number of results to 10
# 'term={name}' dynamically inserts the artist's name into the search term
response = requests.get(f'https://itunes.apple.com/search?entity=song&limit=10&term={name}')

# Parse the JSON response from the API
# 'response.json()' converts the response to a dictionary (Python's equivalent to a JSON object)
o = response.json()

# Loop through the 'results' list from the parsed JSON data
for result in o['results']:
    # Print the name of each track (song) found in the search results
    print(result['trackName'])
