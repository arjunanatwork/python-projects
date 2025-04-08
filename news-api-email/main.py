import requests

api_key = "f183118abb91490abac45a53f170110a"
url = ("https://newsapi.org/v2/everything?q=tesla&"
       "from=2025-03-08&sortBy=publishedAt&apiKey=f183118abb91490abac45a53f170110a")

request = requests.get(url)
content = request.text