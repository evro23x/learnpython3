import requests


def get_weather(url):
    result = requests.get(url)
    if result.status_code == 200:
        return result.json()
    else:
        print("Что-то пошло не так, сервер вернул status_code = {}".format(result.status_code))

if __name__ == "__main__":
    data = get_weather("http://api.data.mos.ru/v1/datasets/2009/rows")
    print(data)
