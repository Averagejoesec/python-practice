import requests
from bs4 import BeautifulSoup
import sqlite3

# ✅ Fetches data from the website
URL = "http://books.toscrape.com/"
response = requests.get(URL)
soup = BeautifulSoup(response.content, "html.parser")
books = soup.find_all("article", class_="product_pod")

# ✅ Extracts each book’s title and price from the main page.
list_of_books = []
for article in books:
    title = article.h3.a["title"]
    price = article.find("p", class_="price_color").text.strip()
    book = (title, price)
    list_of_books.append(book)

# ✅ Saves this data into a local SQLite database file called books.db, inside a table named books with columns title and price.
conn = sqlite3.connect("books.db")
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title TEXT, price TEXT)")
c.executemany("INSERT INTO books (title, price) VALUES (?, ?)", list_of_books)
conn.commit()
conn.close()

# ✅ Prints out the data it found so you can see it before it goes into the database.
print(list_of_books)