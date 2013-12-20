# -*- coding: utf-8 -*-

class Game:

    # dependency injection: quote_instance
    def __init__(self, quote_instance):
        self.quote_instance = quote_instance
        self.nr_quotes = quote_instance.size
        self.quote = ''
        self.author = ''
        self.score = 0
        self.correct = False

    def get_next_quote(self):
        return self.quote_instance.get_next()

    def new_quote_data(self):
        quote = self.get_next_quote()
        self.quote = quote['quote']
        self.author = quote['author']

    def get_quote_text(self):
        return 'Vem sa "{0}"?'.format(self.quote)

    def get_correct_anwer(self):
        return 'Rätt!' if self.correct else 'Fel!'


    def do_answer(self, answer):
        if answer.strip().lower() == self.author.lower():
            self.score += 1
            self.correct = True
        else:
            self.correct = False
        return self.correct

