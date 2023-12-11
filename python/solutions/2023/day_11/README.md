# Day 11 (2023)

`Cosmic Expansion` ([prompt](https://adventofcode.com/2023/day/11))

Another easy one. First collect the positions of all galaxies and compute the empty rows/columns by subtracting the set
of x/y positions of all galaxies from the set of all possible rows/columns. Then iterate over all combinations of
galaxies and compute the distance without expansion (which is the L1-norm) and the number of empty rows/columns that are
traversed by taking the set intersection between the range of traversed rows/columns and the set of empty rows/columns.

## Part 1

The solution is the sum of the distances without expansion and the number of traversed empty rows/columns.

## Part 2

The solution is the sum of the distances without expansion and the number of traversed empty rows/columns multiplied
by `10000000 - 1 = 999999`.
