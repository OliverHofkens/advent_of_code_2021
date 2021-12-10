import std.stdio, std.conv, std.array;

void main() {
    int[12] count_zero;
    int[12] count_one;

    foreach (line; stdin.byLine) {
        foreach (i, bit; line) {
            if (bit == '0') {
                count_zero[i] += 1;
            } else if (bit == '1') {
                count_one[i] += 1;
            }
        }
    }

    auto gamma_rate = 0;
    auto epsilon_rate = 0;

    foreach (i; 0..count_zero.length){
        if (count_one[i] > count_zero[i]){
            gamma_rate = (gamma_rate << 1) | 1;
            epsilon_rate = epsilon_rate << 1;
        } else {
            gamma_rate = gamma_rate << 1;
            epsilon_rate = (epsilon_rate << 1) | 1;
        }
    }

    writeln(gamma_rate * epsilon_rate);
}
