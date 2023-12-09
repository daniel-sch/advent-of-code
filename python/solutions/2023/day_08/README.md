# Day 8 (2023)

`Haunted Wasteland` ([prompt](https://adventofcode.com/2023/day/8))

## Part 1

Part 1 is trivial to solve, just follow the directions until the goal is reached.

## Part 2

Brute forcing the solution (just follow the instructions from all starting points in parallel until all goal nodes are
reached simultaneously) takes very long, so a smarter solution is needed.

Due to the finite number of states (position and index into the instructions) each path needs to loop eventually. A loop
is found if a previous state is encountered again. Luckily the input was engineered, so that for an input with a cycle
of length `l` the goal state is reached exactly (and only) after `l` steps from the start. For this reason the `i`-th
ghost reaches the goal at `k_i * l_i`. The solution to the puzzle is thus the least common multiple of all `l_i`.

A more thorough investigation can be
found [on reddit](https://www.reddit.com/r/adventofcode/comments/18e6vdf/2023_day_8_part_2_an_explanation_for_why_the/).
