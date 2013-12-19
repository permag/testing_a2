# -*- coding: utf-8 -*-

import sys, json, random

class Quote:
	
    def __init__(self):
        # init
        self.current = -1
        self.quotes_data = []
        self.size = 0
        #
        self.quotes_data = self.get_shuffle_data(self.get_data())
        self.size = len(self.quotes_data)

    def get_data(self, file_path=None):
        if not file_path:
            file_path = 'app/data.json'
        try:
            with open(file_path) as json_data:
                data = json.load(json_data)
        except IOError:
            raise
        return data

    def get_shuffle_data(self, data):
        random.shuffle(data)
        return data

    def get_next(self):
        self.current += 1
        curr_quote = self.quotes_data[self.current]
        return {
                'quote': str(curr_quote['quote'].encode('utf-8')), 
                'author': str(curr_quote['author'].encode('utf-8'))
                }
