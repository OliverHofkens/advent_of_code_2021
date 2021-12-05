import std.stdio, std.range, std.conv;

void main () {
    //Start off arbitrarily large, so the first measurement is not counted as an
    //increase.
    auto last_measurement = 1_000_000;
    auto num_increases = 0;

    foreach (line; stdin.byLine) {
        auto measurement = to!int(line);
        if (measurement > last_measurement) {
            num_increases += 1;
        }
        last_measurement = measurement;
    }

    writeln(num_increases);
}
