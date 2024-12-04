import requests


def get_weather(city):
    url_template = 'https://wttr.in/{}?M&n&q&T&lang=ru'
    url_city = url_template.format(city)
    response_city = requests.get(url_city)
    response_city.raise_for_status()
    return response_city.text


def main():
    print(
        get_weather('Лондон'),
        get_weather('Шереметьево'),
        get_weather('Череповец')
    )


if __name__ == '__main__':
    main()
