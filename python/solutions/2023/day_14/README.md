# Day 14 (2023)

`Parabolic Reflector Dish` ([prompt](https://adventofcode.com/2023/day/14))

## Part 1

The first part can be solved by tracking the northernmost position that a round rock can be shifted to. It will start at
0 (all the way to the north) and increases by 1 for each round rock that is shifted. When a cubed rock is encountered,
the position is reset to the position directly south of the cubed rock.

## Part 2

A full round can be computed by shifting the rocks to the north, rotating everything by 90 degrees and then repeating
this process 4 times (for each direction).

Because it takes too long to compute 1000000000 rounds, a more efficient method has to be found. Due to the finite
number of possible states, a cycle of repeating rounds has to occur eventually. To detect this, the hash of the map is
saved to a dictionary together with the round counter for each round. When the hash is already in the dictionary, the
number of rounds remaining until the final state can be computed.
