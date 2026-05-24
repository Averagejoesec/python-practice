import requests
from bs4 import BeautifulSoup
import sqlite3

URL = "http://books.toscrape.com/"
response = requests.get(URL)
soup = BeautifulSoup(response.content, "html.parser")
books = soup.find_all("article", class_="product_pod")

def convert_to_euros(price):
    pounds = float(price.replace("£", ""))
    euros = round(pounds * 1.16, 2)
    price_in_euros = "€" + str(euros)
    return price_in_euros


def get_books():
    list_of_books = []
    for article in books:
        title = article.h3.a["title"]
        price = article.find("p", class_="price_color").text.strip()
        converted_price = convert_to_euros(price)
        book = (title, converted_price)
        list_of_books.append(book)
    print(list_of_books)
    return list_of_books


def write_to_db(list_of_books):
    conn = sqlite3.connect("books.db")
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title TEXT, price TEXT)")
    c.executemany("INSERT INTO books (title, price) VALUES (?, ?)", list_of_books)
    conn.commit()
    conn.close()


if __name__ == "__main__":
    get_books()