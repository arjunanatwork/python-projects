import requests

api_key = "f183118abb91490abac45a53f170110a"
url = ("https://newsapi.org/v2/everything?q=tesla&"
       "from=2025-03-08&sortBy=publishedAt&apiKey=f183118abb91490abac45a53f170110a")

# Make the request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
for article in content['articles']:
    print(article['title'])
    print(article['description'])