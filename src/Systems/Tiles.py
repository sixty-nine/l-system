from .. import Grammar, Symbols, Rules

class Tiles(Grammar.SimpleGrammar):
    """
    http://paulbourke.net/fractals/tiles/
    """

    def __init__(self):
        super(Tiles, self).__init__('F+F+F+F', ['F=FF+F-F+F+FF'])
