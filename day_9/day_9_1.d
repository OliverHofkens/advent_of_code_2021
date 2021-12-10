import std.stdio, std.conv, std.array, std.algorithm;

void main() {
    uint[][] depth_map = array(
            stdin.byLine.map!(
                // Char to int conversion:
                line => array(line.map!(x => x - '0'))
            )
        );

    uint total = 0;

    foreach(i, row; depth_map) {
        foreach(j, col; row) {
            uint north = i == 0 ? uint.max : depth_map[i - 1][j];
            uint south = i == depth_map.length - 1 ? uint.max : depth_map[i + 1][j];
            uint east = j == row.length - 1 ? uint.max : depth_map[i][j + 1];
            uint west = j == 0 ? uint.max : depth_map[i][j - 1];

            if (col < north && col < south && col < east && col < west) {
                total += 1 + col;
            }
        }
    }

    writeln(total);
}
