# -*- coding: utf-8 -*-
from app.game import *
from app.quote import *

def main():
    print "Welcome."
    game = Game(Quote())
    print game.get_next_quote()




# Run program
if __name__ == '__main__':
    main()