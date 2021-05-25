import json
import requests

LINK = 'https://en.wikipedia.org/wiki/'


class Wiki:
    def __init__(self, file):
        self.file = file

    def __iter__(self):
        with open(self.file, 'r') as file:
            countries = json.load(file)

        country_list = []
        for name in countries:
            country_list.append(name['name']['common'])
        self.country = iter(country_list)
        return self

    def __next__(self):
        country = next(self.country)

        with requests.Session() as s:
            resp = s.get(LINK + country)
            if resp.status_code != 200:
                raise StopIteration

        return f'{country}, {LINK + country}\n'


if __name__ == '__main__':
    for c in Wiki('countries.json'):
        with open('links.txt', 'a') as f:
            f.write(c)
