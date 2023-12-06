use advent_of_code::get_relaxed::GetRelaxed;
use lazy_static::lazy_static;
use regex::Regex;
use std::ops::Range;

advent_of_code::solution!(3);

lazy_static! {
    static ref NUMBER_REGEX: Regex = Regex::new(r"\d+").unwrap();
    static ref SYMBOL_REGEX: Regex = Regex::new(r"[^\d\.\s]").unwrap();
    static ref STAR_REGEX: Regex = Regex::new(r"\*").unwrap();
}

fn is_symbol_adjacent(lines: &Vec<&str>, line_idx: usize, span: Range<usize>) -> bool {
    lines
        .get_relaxed(line_idx as i32 - 1..=line_idx as i32 + 1)
        .iter()
        .any(|line| {
            SYMBOL_REGEX.is_match(line.get_relaxed(span.start as i32 - 1..span.end as i32 + 1))
        })
}

fn adjacent_numbers(lines: &Vec<&str>, line_idx: usize, col_idx: usize) -> Vec<u32> {
    lines
        .get_relaxed(line_idx as i32 - 1..=line_idx as i32 + 1)
        .iter()
        .map(|line| {
            NUMBER_REGEX
                .captures_iter(line)
                .map(|c| c.get(0).unwrap())
                .filter(|m| {
                    m.range().start as i32 - 1 <= col_idx as i32 && col_idx < m.range().end + 1
                })
                .map(|m| m.as_str().parse::<u32>().unwrap())
        })
        .flatten()
        .collect()
}

pub fn part_one(input: &str) -> Option<u32> {
    let lines: Vec<&str> = input.lines().collect();
    Some(
        lines
            .iter()
            .enumerate()
            .map(|(idx, line)| {
                NUMBER_REGEX
                    .captures_iter(line)
                    .map(|c| c.get(0).unwrap())
                    .filter(|m| is_symbol_adjacent(&lines, idx, m.range()))
                    .map(|m| m.as_str().parse::<u32>().unwrap())
                    .sum::<u32>()
            })
            .sum(),
    )
}

pub fn part_two(input: &str) -> Option<u32> {
    let lines: Vec<&str> = input.lines().collect();
    Some(
        lines
            .iter()
            .enumerate()
            .map(|(line_idx, line)| {
                STAR_REGEX
                    .captures_iter(line)
                    .map(|c| {
                        let m = c.get(0).unwrap();
                        adjacent_numbers(&lines, line_idx, m.range().start)
                    })
                    .filter(|numbers| numbers.len() == 2)
                    .map(|numbers| numbers[0] * numbers[1])
                    .sum::<u32>()
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
        assert_eq!(result, Some(4361));
    }

    #[test]
    fn test_part_two() {
        let result = part_two(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, Some(467835));
    }
}
