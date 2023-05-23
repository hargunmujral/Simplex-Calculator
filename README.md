# Simplex Calculator

Uses canonical form between iterations to generate simplex solution. Works only for feasible LPs, and can detect unbounded and optimal solutions. Follows Bland's rule!!

I made this because I could not find any canonical method calculators online. All of them used Tableau method, plus they did not follow Bland's rule.

## Sample input:

```
    # Define the matrix A
    A = np.array([[1, 1, 2, 0], [0, 1, 1, 1]])

    # Define the vector b
    b = np.array([2, 5])

    # Define the vector c
    c = np.array([0, 1, 3, 0])

    # Define the constant k at the start
    k = 0

    # Define a basis
    basis = [2, 4]

    # Call the function
    simplex_with_blands_rule(A, b, c, k, basis)
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
