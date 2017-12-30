from .. import Grammar, Symbols, Rules

class Algae2(Grammar.SimpleGrammar):
    """
    http://paulbourke.net/fractals/lsys_algae_a/
    """

    def __init__(self):
        super(Algae2, self).__init__(
            'aF',
            [
                'a=FFFFFv[+++h][---q]fb',
                'b=FFFFFv[+++h][---q]fc',
                'c=FFFFFv[+++fa]fd',
                'd=FFFFFv[+++h][---q]fe',
                'e=FFFFFv[+++h][---q]fg',
                'g=FFFFFv[---fa]fa',
                'h=ifFF',
                'i=fFFF[--m]j',
                'j=fFFF[--n]k',
                'k=fFFF[--o]l',
                'l=fFFF[--p]',
                'm=fFn',
                'n=fFo',
                'o=fFp',
                'p=fF',
                'q=rfF',
                'r=fFFF[++m]s',
                's=fFFF[++n]t',
                't=fFFF[++o]u',
                'u=fFFF[++p]',
                'v=Fv'
            ]
        )
