from .. import Grammar, Symbols, Rules

class Levy(Grammar.SimpleGrammar):
    """
    https://en.wikipedia.org/wiki/L%C3%A9vy_C_curve
    """

    def __init__(self):
        super(Levy, self).__init__('F', ['F=+F--F+'])