use regex::Regex;
use std::fs::File;
use std::io::{BufRead, BufReader};

fn main() {
    let numbers = vec![
        "_", "1", "2", "3", "4", "5", "6", "7", "8", "9", "_", "one", "two", "three", "four",
        "five", "six", "seven", "eight", "nine",
    ];
    let first_number_regex = Regex::new(format!("({})", numbers.join("|")).as_str()).unwrap();
    let last_number_regex = Regex::new(format!("(?s:.*)({})", numbers.join("|")).as_str()).unwrap();

    let filename = "../input.txt";
    let file = File::open(filename).unwrap();
    let mut result = 0;
    for line in BufReader::new(file).lines() {
        let line = line.unwrap();
        let first_num = &first_number_regex.captures(line.as_str()).unwrap()[0];
        let last_num = &last_number_regex.captures(line.as_str()).unwrap()[1];
        let first_num_int = numbers.iter().position(|&x| x == first_num).unwrap() % 10;
        let last_num_int = numbers.iter().position(|&x| x == last_num).unwrap() % 10;
        result += first_num_int * 10 + last_num_int;
    }
    println!("{result}");
}
