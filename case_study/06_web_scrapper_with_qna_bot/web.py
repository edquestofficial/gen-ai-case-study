import requests
from bs4 import BeautifulSoup
import os
import urllib

# The website URL to scrape
url = ""

# The directory to store files in local system
output_dir = ""

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Fetch the page
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find all links to .html files
links = soup.find_all('a', href=True)

for link in links:
    href = link['href']
    
    # If it's a .html file
    if href.endswith('.html'):
        # Make a full URL if necessary
        if not href.startswith('http'):
            href = urllib.parse.urljoin(url, href)
            
        # Fetch the .html file
        file_response = requests.get(href)
        
        # Parse the HTML content
        file_soup = BeautifulSoup(file_response.text, 'html.parser')
        
        # Extract textual content
        text_content = file_soup.get_text()
        
        # Write it to a .txt file
        file_name = os.path.join(output_dir, os.path.basename(href).replace('.html', '.txt'))
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(text_content)
