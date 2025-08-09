# scraper.py
import requests
from bs4 import BeautifulSoup
import csv

url = "http://books.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

books = soup.select(".product_pod")
data = []

for book in books:
    title = book.h3.a['title']
    price = book.select_one(".price_color").text
    data.append([title, price])

# Save to CSV
with open("books.csv", "w", newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(["Title", "Price"])
    writer.writerows(data)
print("Data scraped and saved to books.csv")
# End of scraper.py 