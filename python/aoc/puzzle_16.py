#!/usr/bin/env python

import sys


def main():
    total = 0

    for line in sys.stdin.readlines():
        uniq, to_guess = line.split("|")
        uniq_digits = [set(letters) for letters in uniq.split()]
        guess_digits = [set(letters) for letters in to_guess.split()]

        mapping = [None] * 10

        # Iterative process!
        while not all(mapping):
            for d in uniq_digits:
                try:
                    match len(d):
                        case 2:
                            mapping[1] = d
                        case 3:
                            mapping[7] = d
                        case 4:
                            mapping[4] = d
                        case 5:
                            # The 3 is the only 5-length that contains 1 completely:
                            if mapping[1] <= d:
                                mapping[3] = d
                            # 3-4 gives the left upper segment, which only appears here for 5:
                            elif mapping[4] - mapping[3] <= d:
                                mapping[5] = d
                            else:
                                mapping[2] = d
                        case 6:
                            # If both 1 and 5 are inside, it has to be 9
                            if (mapping[5] | mapping[1]) <= d:
                                mapping[9] = d
                            # If the 5 is contained, it has to be the 6
                            elif mapping[5] <= d:
                                mapping[6] = d
                            else:
                                mapping[0] = d
                        case 7:
                            mapping[8] = d
                        case _:
                            raise NotImplementedError(len(d))
                except TypeError as e:
                    # Something we just don't know yet!
                    continue

        out_digits = "".join(str(mapping.index(dig_set)) for dig_set in guess_digits)
        total += int(out_digits)

    print(total)

if __name__ == "__main__":
    main()
