# -*- coding: utf-8 -*-

import sys, json, random

class Quote:
	
    def __init__(self):
        # init
        self.current = -1
        self.quotes_data = []
        self.quote_count = 0
        #
        self.quotes_data = self.get_shuffle_data(self.get_data())
        self.quote_count = len(self.quotes_data)
        

    def get_data(self, file_path=None):
        if not file_path:
            file_path = 'src/data.json'
        try:
            with open(file_path) as json_data:
                data = json.load(json_data)
        except IOError:
            raise
        return data


    def get_shuffle_data(self, data):
        if data:
            random.shuffle(data)
            return data
        else:
            raise Exception('No data.')


    def get_next(self):
        self.current += 1
        curr_quote = self.quotes_data[self.current]
        authors = []
        for a in curr_quote['author']:     
            authors.append(str(a).encode('utf-8'))
        return {'quote': str(curr_quote['quote'].encode('utf-8')), 
                'author': authors}
