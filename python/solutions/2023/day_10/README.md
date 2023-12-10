# Day 10 (2023)

`Pipe Maze` ([prompt](https://adventofcode.com/2023/day/10))

## Part 1

The strategy here is to follow the pipes from the start and count the steps needed to get back to the starting point.
The result is then the number of steps divided by two.

Special care is needed for the starting point, because the pipe type there is not known. In order to determine the pipe
type, the neighbouring pipes that feed back to the starting point are determined and the appropriate pipe type is
chosen.

The pipes that belong to the loop are collected to make solving part 2 easier.

## Part 2

Counting the number of enclosed spaces can be done for each line individually by only counting spaces where an odd
number of pipes have been crossed. The difficult part are horizontal pipes, because they are only crossed if the pipe
leaves in a different direction than it entered. This can be solved with a state machine.
