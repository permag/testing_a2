import sys, json, random

class Quote:
	
    def __init__(self):
		pass

    def get_data(self):
        with open('app/data.json') as json_data:
            data = json.load(json_data)
        return data

    def get_shuffle_data(self, data):
        random.shuffle(data)
        return data
