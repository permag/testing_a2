
class Game:

    quote_obj = None

    # dependency injection: quote_obj
    def __init__(self, quote_obj):
        self.quote_obj = quote_obj
        self.get_next_quote()

    def get_next_quote(self):
        return self.quote_obj.get_next()