// arraydeque = "0.4"

extern crate arraydeque;

use arraydeque::{ArrayDeque, Wrapping};
use std::{io, io::prelude::*};

fn main() {
    let mut last_measurement = usize::MAX;
    let mut num_increases: usize = 0;

    let mut ring_buf: ArrayDeque<[_; 3], Wrapping> = ArrayDeque::new();

    let stdin = io::stdin();
    let mut lines = stdin.lock().lines();

    // Initialize the ring buffer:
    for line in lines.by_ref().take(3) {
        ring_buf.push_back(line.unwrap().parse().unwrap());
    }

    for line in lines {
        ring_buf.push_back(line.unwrap().parse().unwrap());
        let moving_sum: usize = ring_buf.iter().sum();
        if moving_sum > last_measurement {
            num_increases += 1;
        }
        last_measurement = moving_sum;
    }

    println!("{}", num_increases);
}
