use std::fs::File;
use std::io::{BufRead, BufReader};

fn main() {
    let filename = "../input.txt";
    let file = File::open(filename).unwrap();
    let mut result = 0;
    for line in BufReader::new(file).lines() {
        let numbers: Vec<u32> = line
            .unwrap()
            .chars()
            .filter_map(|c| c.to_digit(10))
            .collect();
        result += numbers.first().unwrap() * 10 + numbers.last().unwrap();
    }
    println!("{result}");
}
