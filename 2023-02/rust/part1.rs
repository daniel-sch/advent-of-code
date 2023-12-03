use regex::Regex;
use std::collections::HashMap;
use std::fs::read_to_string;

fn run(filename: &str) -> usize {
    let max_cubes = HashMap::from([("red", 12), ("green", 13), ("blue", 14)]);
    let cube_regex = Regex::new(r"(\d+) (\w+)").unwrap();

    read_to_string(filename)
        .unwrap()
        .lines()
        .enumerate()
        .filter(|(_, line)| {
            cube_regex
                .captures_iter(line)
                .all(|c| max_cubes[&c[2]] >= c[1].parse::<i32>().unwrap())
        })
        .map(|(idx, _)| idx + 1)
        .sum()
}

fn main() {
    let result = run("../input.txt");
    println!("{result}");
}
