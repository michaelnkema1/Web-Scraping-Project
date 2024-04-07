import requests
from bs4 import BeautifulSoup
import sqlite3

# URL of the website to scrape
url = 'https://citinewsroom.com/2024/04/samsung-brings-ai-to-more-galaxy-devices/'

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Extract specific data from the HTML
# For example, to extract all the links on the page
links = []
for link in soup.find_all("a"):
    links.append(link.get("href"))

conn = sqlite3.connect('links.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS products (title TEXT, price REAL)''')

conn.commit()
conn.close()
