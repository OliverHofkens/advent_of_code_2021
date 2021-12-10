use std::{io, io::prelude::*};

fn main() {
    let mut last_measurement = usize::MAX;
    let mut num_increases: usize = 0;

    for line in io::stdin().lock().lines() {
        let measurement: usize = line.unwrap().parse().unwrap();
        if measurement > last_measurement {
            num_increases += 1;
        }
        last_measurement = measurement;
    }

    println!("{}", num_increases);
}
