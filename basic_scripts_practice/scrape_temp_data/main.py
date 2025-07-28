import requests as rq
import selectorlib
from datetime import datetime

URL = "https://programmer100.pythonanywhere.com/"
OUTPUT_FILE = "basic_scripts_practice/scrape_temp_data/output.txt"
NOW = datetime.now()

def scrape(url):
    response = rq.get(url)
    source = response.text
    return source


def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("basic_scripts_practice/scrape_temp_data/extract.yaml")
    value = extractor.extract(source)["temp"]
    return value


def save_temp(temp):
    with open(OUTPUT_FILE, 'a') as file:
        file.write(f"{NOW}, {temp}\n")

if __name__ == "__main__":
    scraped_scource = scrape(URL)
    temp = extract(scraped_scource)
    save_temp(temp)