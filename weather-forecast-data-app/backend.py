import requests

API_KEY = "9380937a0133d3f11cd4644d8a274dbe"

def get_data(place, forecast_days=None):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data =  response.json()
    filtered_data = data["list"]
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]
    return filtered_data

if __name__ == "__main__":
    print(__name__)