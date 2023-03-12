import requests
from bs4 import BeautifulSoup
import csv

# Set the URL to scrape
url = 'https://www.zoopla.co.uk/to-rent/property/3-bedrooms/south-west-england/'

# Set headers to mimic a browser request
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}

# Send a GET request to the URL and retrieve the HTML content
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

# Extract all the property listings from the HTML content
property_listings = soup.find_all('div', {'class': 'listing-results-wrapper'})

# Create a CSV file to store the property data
with open('zoopla_properties.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)

    # Write the header row to the CSV file
    writer.writerow(['Address', 'Price', 'Description', 'Agent', 'Telephone'])

    # Loop through each property listing and extract the relevant data
    for property_listing in property_listings:
        # Check if the property has 3 bedrooms
        bedrooms = property_listing.find('span', {'class': 'num-icon num-beds'}).text.strip()
        if bedrooms != '3':
            continue
        
        # Extract the address, price, description, agent name, and agent telephone number
        address = property_listing.find('a', {'class': 'listing-results-address'}).text.strip()
        price = property_listing.find('p', {'class': 'listing-results-price'}).text.strip()
        description = property_listing.find('a', {'class': 'listing-results-attr'}).text.strip()
        agent = property_listing.find('p', {'class': 'listing-results-marketed'}).text.strip()
        telephone = property_listing.find('span', {'class': 'agent_phone'}).text.strip()

        # Write the data to the CSV file
        writer.writerow([address, price, description, agent, telephone])
