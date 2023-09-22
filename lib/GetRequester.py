import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content
        pass

    def load_json(self):
        data_list = []
        data = json.loads(self.get_response_body())
        for dat in data:
            data_list.append(dat)
        return data_list
        pass
People = GetRequester("https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json")
print(People.load_json)