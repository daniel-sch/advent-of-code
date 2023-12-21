# Day 19 (2023)

`Aplenty` ([prompt](https://adventofcode.com/2023/day/19))

## Part 1

Start with the `in` workflow and check the rules for this workflow until one matches, then follow the new workflow.
Repeat until `R` or `A` is reached.

## Part 2

The space of possible parts is tracked in a dictionary. Each rule splits the space of possible parts into two sections.
For the section where the condition is true, the function is called recursively for the new workflow. For the part where
the condition is false, the next rule is evaluated until the default rule is reached. When the `R` workflow is reached,
a value of 0 is returned and when the `A` workflow is reached, the volume of the section is returned.
