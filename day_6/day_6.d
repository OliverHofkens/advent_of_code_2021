import std.stdio, std.conv, std.array, std.algorithm;
import std.string: stripRight;

void main() {
    immutable ITERATIONS = 256;

    ulong[9] counts = 0;
    int[] initial = array(readln().stripRight!().split(',').map!(to!int));

    foreach (n; initial) {
        counts[n] += 1;
    }

    foreach (i; 0..ITERATIONS) {
        auto to_add = counts[0];
        // Rotate -1:
        bringToFront(counts[0 .. 1], counts[1 .. $]);
        // Previous 0's become 6's:
        counts[6] += counts[$ - 1];
        writeln(counts);
    }

    writeln(counts[].sum());
}
