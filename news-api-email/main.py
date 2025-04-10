import requests
from datetime import datetime
from send_email import send_email

topic = "tesla"
current_date = datetime.now().strftime("%Y-%m-%d")

api_key = "f183118abb91490abac45a53f170110a"
url = ("https://newsapi.org/v2/everything?"
       f"q={topic}&from={current_date}&"
       "sortBy=publishedAt&"
       "apiKey=f183118abb91490abac45a53f170110a&language=en")

# Make the request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
body= ""
for article in content['articles'][:20]:
    if article['title'] is not None and article['description'] is not None:
        body = "Subject: Today's news" + "\n" + body + article['title'] + "\n" + article['description'] + "\n" + article["url"] + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)