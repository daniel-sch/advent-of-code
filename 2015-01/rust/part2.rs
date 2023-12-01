use std::fs;

fn main() {
    let filename = "../input.txt";
    let contents = fs::read_to_string(filename).expect("Should have been able to read the file");

    let mut floor = 0;
    for (i, c) in contents.chars().enumerate() {
        floor += if c == '(' { 1 } else { -1 };
        if floor == -1 {
            println!("{}", i + 1);
            break;
        }
    }
}
