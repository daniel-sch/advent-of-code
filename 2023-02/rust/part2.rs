use regex::Regex;
use std::cmp::max;
use std::collections::HashMap;
use std::fs::read_to_string;

fn run(filename: &str) -> i32 {
    let cube_regex = Regex::new(r"(\d+) (\w+)").unwrap();

    read_to_string(filename)
        .unwrap()
        .lines()
        .map(|line| {
            let mut min_cubes = HashMap::with_capacity(3);
            for c in cube_regex.captures_iter(line) {
                let amount = c[1].parse::<i32>().unwrap();
                min_cubes
                    .entry(c[2].to_string())
                    .and_modify(|e| *e = max(amount, *e))
                    .or_insert(amount);
            }
            min_cubes.values().product::<i32>()
        })
        .sum()
}

fn main() {
    let result = run("../input.txt");
    println!("{result}");
}
