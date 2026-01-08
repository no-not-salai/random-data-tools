# inputer

## What it does
Utilities to generate random numeric data for testing and learning.

## How to use

### Random integer list
`Inputer.intlist(a, b, c)`

Parameters:
- `a`: list length
- `b`: minimum value (inclusive)
- `c`: maximum value (inclusive)

Example:
Inputer.intlist(5, -2, 20)

        [-2, 0, 5, 12, 1]

-----

### Random float list
`Inputer.floatlist(a, b, c, d(optional))`

Parameters:
- `a`: list length
- `b`: minimum value (inclusive)
- `c`: maximum value (inclusive)
- `d`: decimal places (optional, default=2)

Example:

Inputer.floatlist(5, -2, 20)

        [-1.40, 0.01, -1.22, 19.99, 20.00]
