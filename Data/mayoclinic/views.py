from django.shortcuts import render

import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin

# URL of the page to scrape
url = 'https://www.mayocliniclabs.com/articles/resources/algorithms'

# Headers to mimic your specific browser
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1'
}

# Send a request to the website
response = requests.get(url, headers=headers)
response.raise_for_status()  # Check for request errors

# Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find all links that end with .pdf
pdf_links = [urljoin(url, a['href']) for a in soup.find_all('a', href=True) if a['href'].endswith('.pdf')]

# Directory to save the PDFs
os.makedirs('pdfs', exist_ok=True)

# Download each PDF with a custom file name
for i, link in enumerate(pdf_links, start=1):
    pdf_response = requests.get(link, headers=headers)
    pdf_response.raise_for_status()
    
    # Custom file name, e.g., "algorithm_1.pdf", "algorithm_2.pdf", etc.
    file_name = os.path.join('pdfs', f'algorithm_{i}.pdf')
    
    with open(file_name, 'wb') as file:
        file.write(pdf_response.content)
    
    print(f'Downloaded: {file_name}')

print('All PDFs have been downloaded.')

