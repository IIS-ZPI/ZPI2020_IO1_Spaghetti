from urllib.request import urlopen
import json


def read_from_url(url):
    file = urlopen(url)
    result = file.readline()
    return result

def get_dictionary_from_json(url):
    json_txt = read_from_url(url)
    return json.loads(json_txt)


class JsonManager:
    def __init__(self, url):
        self.json_txt = read_from_url(url)
        self.dict = json.loads(self.json_txt)
