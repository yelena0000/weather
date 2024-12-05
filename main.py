import requests


def get_weather(place):
    params = {
        'M': '',
        'n': '',
        'q': '',
        'T': '',
        'lang': 'ru'
    }
    url = f'https://wttr.in/{place}'
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.text


def main():
    cities = [
        'Лондон',
        'Шереметьево',
        'Череповец'
    ]
    for city in cities:
        print(get_weather(city))


if __name__ == '__main__':
    main()
