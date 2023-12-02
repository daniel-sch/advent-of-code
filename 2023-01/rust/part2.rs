use regex::Regex;
use std::fs::read_to_string;

fn run(filename: &str) -> usize {
    let numbers = vec![
        "_", "1", "2", "3", "4", "5", "6", "7", "8", "9", "_", "one", "two", "three", "four",
        "five", "six", "seven", "eight", "nine",
    ];
    let first_number_regex = Regex::new(format!("({})", numbers.join("|")).as_str()).unwrap();
    let last_number_regex = Regex::new(format!("(?s:.*)({})", numbers.join("|")).as_str()).unwrap();

    read_to_string(filename)
        .unwrap()
        .lines()
        .map(|line| {
            let first_num = &first_number_regex.captures(line).unwrap()[0];
            let last_num = &last_number_regex.captures(line).unwrap()[1];
            let first_num_int = numbers.iter().position(|&x| x == first_num).unwrap() % 10;
            let last_num_int = numbers.iter().position(|&x| x == last_num).unwrap() % 10;
            first_num_int * 10 + last_num_int
        })
        .sum()
}

fn main() {
    let result = run("../input.txt");
    println!("{result}");
}
