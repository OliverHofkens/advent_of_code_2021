import std.stdio, std.conv, std.array, std.algorithm;
import std.container: SList;


void main() {
    immutable char[char] closers = [
        ')': '(',
        ']': '[',
        '}': '{',
        '>': '<',
    ];
    immutable uint[char] score_map = [
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137,
    ];

    uint score = 0;
    auto stack = SList!char();

    foreach (line; stdin.byLine) {
        foreach (c; line) {
            if (auto closes = c in closers) {
                auto opener = stack.front();
                stack.removeFront();
                if (opener != *closes){
                    // CORRUPT!
                    score += score_map[c];
                    break;
                }
            } else {
                // Not a closer, so it's an opener:
                stack.insert(c);
            }
        }
    }

    writeln(score);
}
