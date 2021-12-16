#!/usr/bin/env python

import sys
from dataclasses import dataclass
from typing import Iterable, List

from bitarray import bitarray
from bitarray.util import ba2int, hex2ba


@dataclass
class Packet:
    version: int
    type_id: int


@dataclass
class LiteralPacket(Packet):
    value: int


@dataclass
class OperatorPacket(Packet):
    length_type_id: int
    length: int
    children: List[Packet]


def parse_packet(inp):
    type_id = ba2int(inp[3:6])

    if type_id == 4:
        return parse_literal_packet(inp)
    else:
        return parse_operator_packet(inp)


def parse_literal_packet(inp):
    version = ba2int(inp[:3])
    type_id = ba2int(inp[3:6])

    cursor = 6
    literal_bits = bitarray(endian="big")
    while True:
        chunk = inp[cursor : cursor + 5]
        literal_bits.extend(chunk[1:])
        cursor += 5
        if chunk[0] == 0:
            break

    result = ba2int(literal_bits)

    unparsed = inp[cursor:]
    return LiteralPacket(version, type_id, result), unparsed


def parse_operator_packet(inp):
    version = ba2int(inp[:3])
    type_id = ba2int(inp[3:6])
    children = []

    length_type_id = inp[6]
    if length_type_id == 0:
        length = ba2int(inp[7:22])
        unparsed = inp[22 : 22 + length]
        while unparsed:
            child, unparsed = parse_packet(unparsed)
            children.append(child)
        unparsed = inp[22 + length :]
    else:
        length = ba2int(inp[7:18])
        unparsed = inp[18:]
        while len(children) < length:
            child, unparsed = parse_packet(unparsed)
            children.append(child)

    return OperatorPacket(version, type_id, length_type_id, length, children), unparsed


def walk_packet_tree(packet: Packet) -> Iterable[Packet]:
    yield packet
    if isinstance(packet, OperatorPacket):
        for child in packet.children:
            yield from walk_packet_tree(child)


def main():
    code = hex2ba(sys.stdin.readline().strip(), endian="big")
    root_packet, _ = parse_packet(code)

    version_sum = sum(pkt.version for pkt in walk_packet_tree(root_packet))
    print(version_sum)


if __name__ == "__main__":
    main()
