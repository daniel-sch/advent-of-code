# Day 7 (2023)

`Camel Cards` ([prompt](https://adventofcode.com/2023/day/7))

My strategy for this puzzle is to create a class for `Hand` which has comparison operators. This way the python sort
function can be used and the calculation of the final score is trivial. The challenging task is to determine which type
a hand has. This differs slightly for both parts:

## Part 1

Use a `Counter` to determine the count of the two most common cards. Then determining the type becomes a simple match
operation.

## Part 2

For part 2 separate the jokers from the rest of the cards and add their number to the most common card (this will
always give the strongest hand type). Then the match operation from part 1 can be used. 
