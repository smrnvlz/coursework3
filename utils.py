import requests


def get_data(url):
    response = requests.get(url).json()
    print(response)
