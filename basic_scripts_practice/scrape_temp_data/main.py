import requests as rq
import selectorlib
import sqlite3
from datetime import datetime

URL = "https://programmer100.pythonanywhere.com/"
OUTPUT_FILE = "output.txt"
NOW = datetime.now().strftime("%y-%m-%d-%H-%M-%S")

connection = sqlite3.connect("data.db")

def scrape(url):
    response = rq.get(url)
    source = response.text
    return source


def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)["temp"]
    return value


def save_temp(temp):
    row = [NOW, temp]
    cursor = connection.cursor()
    cursor.execute("INSERT INTO temperature VALUES(?,?)", row)
    connection.commit()


if __name__ == "__main__":
    scraped_scource = scrape(URL)
    temp = extract(scraped_scource)
    save_temp(temp)