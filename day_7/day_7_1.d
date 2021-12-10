import std.stdio, std.conv, std.array, std.algorithm, std.math;
import std.string: stripRight;

void main() {
    immutable int[] positions = array(readln().stripRight!().split(',').map!(to!int));

    auto best_cost = double.max;
    foreach (alignment; positions.minElement()..positions.maxElement()) {
        auto fuel_cost = positions.map!(p => fabs(cast(float) p - alignment)).sum();
        if (fuel_cost < best_cost) {
            best_cost = fuel_cost;
        }
    }

    writeln(best_cost.to!int());
}
