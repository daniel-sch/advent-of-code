pub mod get_relaxed;
use crate::get_relaxed::GetRelaxed;

use lazy_static::lazy_static;
use regex::Regex;
use std::fs::read_to_string;
use std::ops::Range;

lazy_static! {
    static ref NUMBER_REGEX: Regex = Regex::new(r"\d+").unwrap();
    static ref SYMBOL_REGEX: Regex = Regex::new(r"[^\d\.\s]").unwrap();
}

fn is_symbol_adjacent(lines: &Vec<&str>, line_idx: usize, span: Range<usize>) -> bool {
    lines
        .get_relaxed(line_idx as i32 - 1..=line_idx as i32 + 1)
        .iter()
        .any(|line| {
            SYMBOL_REGEX.is_match(line.get_relaxed(span.start as i32 - 1..span.end as i32 + 1))
        })
}

fn run(filename: &str) -> i32 {
    let file_content = read_to_string(filename).unwrap();
    let lines: Vec<&str> = file_content.lines().collect();
    lines
        .iter()
        .enumerate()
        .map(|(idx, line)| {
            NUMBER_REGEX
                .captures_iter(line)
                .map(|c| c.get(0).unwrap())
                .filter(|m| is_symbol_adjacent(&lines, idx, m.range()))
                .map(|m| m.as_str().parse::<i32>().unwrap())
                .sum::<i32>()
        })
        .sum()
}

fn main() {
    let result = run("../input.txt");
    println!("{result}");
}
