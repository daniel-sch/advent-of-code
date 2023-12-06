use regex::Regex;

advent_of_code::solution!(1);

pub fn part_one(input: &str) -> Option<u32> {
    Some(
        input
            .lines()
            .map(|line| {
                let numbers: Vec<u32> = line.chars().filter_map(|c| c.to_digit(10)).collect();
                numbers.first().unwrap() * 10 + numbers.last().unwrap()
            })
            .sum(),
    )
}

pub fn part_two(input: &str) -> Option<u32> {
    let numbers = vec![
        "_", "1", "2", "3", "4", "5", "6", "7", "8", "9", "_", "one", "two", "three", "four",
        "five", "six", "seven", "eight", "nine",
    ];
    let first_number_regex = Regex::new(format!("({})", numbers.join("|")).as_str()).unwrap();
    let last_number_regex = Regex::new(format!("(?s:.*)({})", numbers.join("|")).as_str()).unwrap();

    Some(
        input
            .lines()
            .map(|line| {
                let first_num = &first_number_regex.captures(line).unwrap()[0];
                let last_num = &last_number_regex.captures(line).unwrap()[1];
                let first_num_int = numbers.iter().position(|&x| x == first_num).unwrap() % 10;
                let last_num_int = numbers.iter().position(|&x| x == last_num).unwrap() % 10;
                first_num_int * 10 + last_num_int
            })
            .sum::<usize>() as u32,
    )
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_one() {
        let result = part_one(
            "1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet",
        );
        assert_eq!(result, Some(142));
    }

    #[test]
    fn test_part_two() {
        let result = part_two(
            "two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
",
        );
        assert_eq!(result, Some(281));
    }
}
