
class Game:

    quote_instance = None

    # dependency injection: quote_instance
    def __init__(self, quote_instance):
        self.quote_instance = quote_instance
        self.get_next_quote()

    def get_next_quote(self):
        return self.quote_instance.get_next()