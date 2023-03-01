# Simplex Calculator

Uses canonical form between iterations to generate simplex solution. Works only for feasible LPs, and can detect unbounded and optimal solutions. Follows Blank's rule!!

I made this because I could not find any canonical method calculators online. All of them used Tableau method, plus they did not follow Blank's rule.

## Sample input:

```
    A = np.array([
        [1, -1, 1, 0, 0, 0, 0],
        [1, 0, 0, 1, 0, 0, 0],
        [4, 3, 0, 0, 1, 0, 0],
        [1, 3, 0, 0, 0, 1, 0],
        [-2, 3, 0, 0, 0, 0, 1]
    ])
    b = np.array([2, 6, 36, 18, 9])
    c = np.array([2, 7, 0, 0, 0, 0, 0])
    k = 0  # some value
    basis = [1, 4, 5, 6, 7]  # some basis in the form [a,b,c]
    simplex_with_blanks_rule(A, b, c, k, basis)
```

## Instructions:

super straightforward:

```
pip install -r requirements.txt
```

then fill in your inputs for A, b, c, k, basis
<br>
then run:

```
python ./simplex.py
```

## Known bugs:

- floating point precision to 3-4 decimals
- sometimes 0 becomes -0

## To implement:

- support for two-phase simplex
- remove floating point workarounds (1e-3 instead of 0, 1e6 as max value)
- infeasibility detection (low priority)
- tableau method option
