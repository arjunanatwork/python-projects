import smtplib
import ssl
import time

import requests
import selectorlib
import sqlite3

URL = "http://programmer100.pythonanywhere.com/tours/"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

connection = sqlite3.connect('data.db')

def scrape(url):
    """Scrape the page source from teh URL"""
    response  = requests.get(url, headers=HEADERS)
    source = response.text
    return source

def extract(source):
    """Extract the data from the source"""
    extractor = selectorlib.Extractor.from_yaml_file("extract.yml")
    value = extractor.extract(source)["tours"]
    return value

def store(extracted):
    row = extracted.split(",")
    row = [items.strip() for items in row]
    cursor = connection.cursor()
    cursor.execute("INSERT INTO events VALUES (?, ?, ?)", row)
    connection.commit()

def read(extracted):
   row = extracted.split(",")
   row = [items.strip() for items in row]
   band, city, date = row
   cursor = connection.cursor()
   cursor.execute("SELECT * FROM events WHERE band=? AND city=? AND date=?", (band, city, date))
   rows = cursor.fetchall()
   return rows

def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "arjunanatwork@gmail.com"
    password = "zyly hnta rutz oegf"

    receiver = "arjunan1991@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

if __name__ == "__main__":
    while True:
        scraped = scrape(URL)
        extracted = extract(scraped)
        print(extracted)

        if extracted != "No upcoming tours":
            row = read(extracted)
            if not row:
                store(extracted)
                send_email(message="Hey there, there is a new tour coming up!")
        time.sleep(2)