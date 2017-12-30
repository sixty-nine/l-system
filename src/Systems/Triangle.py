from .. import Grammar, Symbols, Rules

class Triangle(Grammar.SimpleGrammar):
    """
    http://paulbourke.net/fractals/traingle/
    """

    def __init__(self):
        super(Triangle, self).__init__('F+F+F', ['F=F-F+F'])
