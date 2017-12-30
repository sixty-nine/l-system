# Exploration of Lindenmayer systems

## Draw various L-Systems

```
python demo/demo.py --system <system>
```

Where `<system>` is one of the following: tiles, triangle, hex-gosper, qki, weed,
koch, hilbert, krishna, sierpinski, rings, dragon, crystal, board, algae2

## Examples of L-Systems

Check the `src/Systems` directory.

There are several ways to implement L-Systems. Two good and different examples are:

 * [`algae.py`](https://github.com/sixty-nine/l-system/blob/master/src/Systems/Algae.py)
 * [`algae2.py`](https://github.com/sixty-nine/l-system/blob/master/src/Systems/Algae2.py)

## Koch curve

In extenso:

```
f = Constant('F')
plus = Constant('+')
minus = Constant('-')

r = SimpleRule(f, String([f, plus, f, minus, f, minus, f, plus, f]))

g = Grammar(f, [f, plus, minus], [r])
```

Compact way:

```
g = SimpleGrammar('F', ['F=F+F-F-F+F'])
```

"Too easy" way (only for predefined systems):

```
g = LSystem.Systems.Koch()
```

## Pretty print

```
g = SimpleGrammar('F', ['F=F+F-F-F+F'])
print str(g.pretty())
```

Will output:

```
SimpleGrammar {
  Axiom: F

  Rules:
    F --> F+F-F-F+F
}
```

## Run the tests

```
python tests/runner.py
```
