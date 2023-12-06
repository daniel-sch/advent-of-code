use regex::Regex;
use std::cmp::max;
use std::collections::HashMap;

advent_of_code::solution!(2);

pub fn part_one(input: &str) -> Option<u32> {
    let max_cubes = HashMap::from([("red", 12), ("green", 13), ("blue", 14)]);
    let cube_regex = Regex::new(r"(\d+) (\w+)").unwrap();

    Some(
        input
            .lines()
            .enumerate()
            .filter(|(_, line)| {
                cube_regex
                    .captures_iter(line)
                    .all(|c| max_cubes[&c[2]] >= c[1].parse::<i32>().unwrap())
            })
            .map(|(idx, _)| idx + 1)
            .sum::<usize>() as u32,
    )
}

pub fn part_two(input: &str) -> Option<u32> {
    let cube_regex = Regex::new(r"(\d+) (\w+)").unwrap();

    Some(
        input
            .lines()
            .map(|line| {
                let mut min_cubes = HashMap::with_capacity(3);
                for c in cube_regex.captures_iter(line) {
                    let amount = c[1].parse::<u32>().unwrap();
                    min_cubes
                        .entry(c[2].to_string())
                        .and_modify(|e| *e = max(amount, *e))
                        .or_insert(amount);
                }
                min_cubes.values().product::<u32>()
            })
            .sum(),
    )
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_one() {
        let result = part_one(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, Some(8));
    }

    #[test]
    fn test_part_two() {
        let result = part_two(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, Some(2286));
    }
}
