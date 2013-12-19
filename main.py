# -*- coding: utf-8 -*-
from app.game import *
from app.quote import *

def main():
    game = Game(Quote())

    print '\n******* Välkommen till "Vem sa?" *******'
    count = 0
    while game.nr_quotes > count:
        count += 1
        game.new_quote_data()
        # Who said...?
        print '\n', game.get_quote_text()
        answer = raw_input()
        game.do_answer(answer)
        print game.get_correct_anwer()

    print '\nDu fick {0} poäng.'.format(game.score)




# Run program
if __name__ == '__main__':
    main()