# Day 12 (2023)

`Hot Springs` ([prompt](https://adventofcode.com/2023/day/12))

The first approach was to do exhaustive search and replace all `?` with all possible combinations of `.` and `#`. This
however is way too inefficient and will take forever for part 2.

A more efficient solution is to replace the first `?` with both `.` and `#` and call the same function recursively. At
the beginning of the function, a regex is used to check whether the string begins with a completed group (i.e., a group
of `#` which is followed by a `.`). If it does and the length of the group matches the first element of the `runs`
tuple, the first group is removed from the string and the `runs` tuple. If the string begins with a completed group,
whose length does not match the first relement of the `runs` tuple, the function immediately returns `0`, as all
possible solutions with this start will be invalid. For added performance the `functools.cache` function is used.

## Part 1

Run the algorithm with the unmodified input.

## Part 2

Run the algorithm with the inputs repeated 5 times.
