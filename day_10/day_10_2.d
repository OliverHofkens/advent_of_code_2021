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
        '(': 1,
        '[': 2,
        '{': 3,
        '<': 4,
    ];

    ulong[] all_scores;
    auto stack = SList!char();

    foreach (line; stdin.byLine) {
        foreach (c; line) {
            if (auto closes = c in closers) {
                auto opener = stack.front();
                stack.removeFront();
                if (opener != *closes){
                    // CORRUPT!
                    stack.clear();
                    break;
                }
            } else {
                // Not a closer, so it's an opener:
                stack.insert(c);
            }
        }

        if (!stack.empty()){
            ulong score = 0;
            // The line is incomplete, add the missing characters:
            while (!stack.empty()) {
                auto to_close = stack.front();
                stack.removeFront();
                score = score * 5 + score_map[to_close];
            }
            all_scores ~= score;
        }
    }

    writeln(all_scores.sort!"a < b"()[all_scores.length / 2]);
}
