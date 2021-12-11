import std.stdio, std.conv, std.array, std.algorithm, std.range;


void main() {
    uint[][] energy = array(
            stdin.byLine.map!(
                // Char to int conversion:
                line => array(line.map!(x => x - '0'))
            )
        );

    for (int step = 0; step < 1000; step++){
        int[][] flashes;

        // First, all energies increase by 1:
        foreach (i, row; energy) {
            row[] += 1;
            foreach (j, col; row) {
                if (col > 9) {
                    flashes ~= cast(int[]) [i, j];
                }
            }
        }

        uint flash_idx = 0;
        while (flash_idx < flashes.length){
            foreach (flash_coord; flashes[flash_idx..$]) {
                auto neighbors = cartesianProduct(
                        iota(flash_coord[0]-1, flash_coord[0]+2),
                        iota(flash_coord[1]-1, flash_coord[1]+2)
                    ).filter!(pt => pt[0] >= 0 && pt[1] >= 0 && pt[0] < energy.length && pt[1] < energy[0].length);
                foreach (pt; neighbors) {
                    energy[pt[0]][pt[1]] += 1;
                    if (energy[pt[0]][pt[1]] > 9 && !canFind(flashes, [pt[0], pt[1]])) {
                        flashes ~= [pt[0], pt[1]];
                    }
                }
                flash_idx += 1;
            }
        }

        if (flashes.length == energy.length * energy[0].length){
            writeln(step + 1);
            break;
        }

        foreach (pt; flashes) {
            energy[pt[0]][pt[1]] = 0;
        }
    }
}
