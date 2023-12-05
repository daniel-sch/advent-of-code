pub mod get_relaxed;
use crate::get_relaxed::GetRelaxed;

use lazy_static::lazy_static;
use regex::Regex;
use std::fs::read_to_string;

lazy_static! {
    static ref NUMBER_REGEX: Regex = Regex::new(r"\d+").unwrap();
    static ref STAR_REGEX: Regex = Regex::new(r"\*").unwrap();
}

fn adjacent_numbers(lines: &Vec<&str>, line_idx: usize, col_idx: usize) -> Vec<i32> {
    lines
        .get_relaxed(line_idx as i32 - 1..=line_idx as i32 + 1)
        .iter()
        .map(|line| {
            NUMBER_REGEX
                .captures_iter(line)
                .filter_map(|c| {
                    let m = c.get(0).unwrap();
                    if m.range().start as i32 - 1 <= col_idx as i32 && col_idx < m.range().end + 1 {
                        Some(m.as_str().parse::<i32>().unwrap())
                    } else {
                        None
                    }
                })
                .collect::<Vec<i32>>()
        })
        .flatten()
        .collect()
}

fn run(filename: &str) -> i32 {
    let file_content = read_to_string(filename).unwrap();
    let lines: Vec<&str> = file_content.lines().collect();
    lines
        .iter()
        .enumerate()
        .map(|(line_idx, line)| {
            STAR_REGEX
                .captures_iter(line)
                .filter_map(|c| {
                    let m = c.get(0).unwrap();
                    let numbers = adjacent_numbers(&lines, line_idx, m.range().start);
                    if numbers.len() == 2 {
                        Some(numbers[0] * numbers[1])
                    } else {
                        None
                    }
                })
                .sum::<i32>()
        })
        .sum()
}

fn main() {
    let result = run("../input.txt");
    println!("{result}");
}
