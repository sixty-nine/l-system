from .. import Grammar, Symbols, Rules

class Board(Grammar.SimpleGrammar):
    """
    http://paulbourke.net/fractals/board/
    """

    def __init__(self):
        super(Board, self).__init__('F+F+F+F', ['F=FF+F+F+F+FF'])
