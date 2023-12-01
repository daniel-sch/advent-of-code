use std::fs;

fn main() {
    let filename = "../input.txt";
    let contents = fs::read_to_string(filename).expect("Should have been able to read the file");

    let up_count = contents.matches("(").count();
    let down_count = contents.matches(")").count();
    let final_floor = up_count - down_count;
    println!("{final_floor}");
}
