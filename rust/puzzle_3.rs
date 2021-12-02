use std::{io, io::prelude::*};

fn main() {
    let mut depth: usize = 0;
    let mut horizontal: usize = 0;

    for line in io::stdin().lock().lines() {
        let l = line.unwrap();
        let (action, amount) = l.split_once(" ").unwrap();
        let amount: usize = amount.parse().unwrap();

        match action {
            "forward" => horizontal += amount,
            "down" => depth += amount,
            "up" => depth -= amount,
            _ => (),
        };
    }

    println!("{}", depth * horizontal);
}
