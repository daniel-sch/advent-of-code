use std::fs::read_to_string;

fn run(filename: &str) -> u32 {
    read_to_string(filename)
        .unwrap()
        .lines()
        .map(|line| {
            let numbers: Vec<u32> = line.chars().filter_map(|c| c.to_digit(10)).collect();
            numbers.first().unwrap() * 10 + numbers.last().unwrap()
        })
        .sum()
}

fn main() {
    let result = run("../input.txt");
    println!("{result}");
}
