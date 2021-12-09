import std.stdio, std.conv, std.array, std.algorithm;


ulong find_basin_size(uint[][] depth_map, size_t low_i, size_t low_j) {
    size_t[][] basin_points = [[low_i, low_j]];
    size_t progress_idx = 0;

    while (progress_idx < basin_points.length) {
        foreach (point; basin_points[progress_idx..$]) {
            size_t i, j;
            i = point[0];
            j = point[1];
            size_t[2] coord;

            if (i > 0 && depth_map[i - 1][j] < 9) {
                coord[] = [i -1, j];
                if (!canFind(basin_points, coord)) {
                    basin_points ~= coord.dup;
                }
            }

            if (i < depth_map.length - 1 && depth_map[i + 1][j] < 9) {
                coord[] = [i +1, j];
                if (!canFind(basin_points, coord)) {
                    basin_points ~= coord.dup;
                }
            }

            if (j < depth_map[0].length - 1 && depth_map[i][j + 1] < 9) {
                coord = [i, j + 1];
                if (!canFind(basin_points, coord)) {
                    basin_points ~= coord.dup;
                }
            }

            if (j > 0 && depth_map[i][j - 1] < 9) {
                coord = [i, j - 1];
                if (!canFind(basin_points, coord)) {
                    basin_points ~= coord.dup;
                }
            }

            progress_idx += 1;
        }
    }
    return basin_points.length;
}


void main() {
    uint[][] depth_map = array(
            stdin.byLine.map!(
                // Char to int conversion:
                line => array(line.map!(x => x - '0'))
            )
        );

    ulong[] basin_sizes;

    foreach(i, row; depth_map) {
        foreach(j, col; row) {
            uint north = i == 0 ? uint.max : depth_map[i - 1][j];
            uint south = i == depth_map.length - 1 ? uint.max : depth_map[i + 1][j];
            uint east = j == row.length - 1 ? uint.max : depth_map[i][j + 1];
            uint west = j == 0 ? uint.max : depth_map[i][j - 1];

            if (col < north && col < south && col < east && col < west) {
                basin_sizes ~= find_basin_size(depth_map, i, j);
            }
        }
    }

    auto top_3 = basin_sizes.topN!"a > b"(3);
    writeln(top_3.reduce!((a, b) => a * b));
}
