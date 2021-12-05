import std.stdio, std.conv, std.array;

void main() {
    auto depth = 0;
    auto horizontal = 0;

    foreach (line; stdin.byLine) {
        auto parts = line.split();
        auto action = parts[0];
        auto amount = to!int(parts[1]);

        switch (action) {
            case "forward":
                horizontal += amount;
                break;
            case "down":
                depth += amount;
                break;
            case "up":
                depth -= amount;
                break;
            default:
                break;
        }
    }

    writeln(depth * horizontal);
}
