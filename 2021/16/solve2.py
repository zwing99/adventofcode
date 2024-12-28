#!/usr/bin/env python

from multiprocessing import process
from struct import pack
import sys

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(filename) as fh:
    lines = [line.strip() for line in fh.readlines()]

hex_map = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}


def process_packet(packet: str, depth=0):
    tabs = "\t" * depth
    print(f"{tabs}Processing packet {packet}")
    packet_ver, packet = packet[:3], packet[3:]
    packet_typ, packet = packet[:3], packet[3:]
    packet_ver = int(packet_ver, 2)
    packet_typ = int(packet_typ, 2)
    print(f"{tabs}Packet version: {packet_ver}, Packet type: {packet_typ}")
    version_sum = packet_ver
    if packet_typ == 4:
        v = ""
        while True:
            n, packet = packet[:5], packet[5:]
            v += n[1:]
            if n[0] == "0":
                break
        v = int(v, 2)
        print(f"{tabs}Literal value", v)
        return packet, packet_ver, packet_typ, version_sum, v
    else:
        l_bit, packet = packet[:1], packet[1:]
        packet_values = []
        if l_bit == "0":
            lng, packet = packet[:15], packet[15:]
            lng = int(lng, 2)
            print(f"{tabs}Packet length", lng)
            sub_packets, packet = packet[:lng], packet[lng:]
            while True:
                sub_packets, sub_packet_ver, sub_packet_type, v_sum, pv = (
                    process_packet(sub_packets[:], depth + 1)
                )
                packet_values.append(pv)
                version_sum += v_sum
                if "1" not in sub_packets:
                    break
        else:
            num_packets, packet = packet[:11], packet[11:]
            num_packets = int(num_packets, 2)
            print(f"{tabs}Number of packets", num_packets)
            for _ in range(num_packets):
                packet, sub_packet_ver, sub_packet_type, v_sum, pv = process_packet(
                    packet[:], depth + 1
                )
                packet_values.append(pv)
                version_sum += v_sum
        match packet_typ:
            case 0:
                v = sum(packet_values)
            case 1:
                v = 1
                for pv in packet_values:
                    v *= pv
            case 2:
                v = min(packet_values)
            case 3:
                v = max(packet_values)
            case 5:
                assert len(packet_values) == 2
                v = 1 if packet_values[0] > packet_values[1] else 0
            case 6:
                assert len(packet_values) == 2
                v = 1 if packet_values[0] < packet_values[1] else 0
            case 7:
                assert len(packet_values) == 2
                v = 1 if packet_values[0] == packet_values[1] else 0
            case _:
                print(f"{tabs}failed")
                exit(1)

        return packet, packet_ver, packet_typ, version_sum, v


def hex_to_bin(hex_str):
    return "".join([hex_map[x] for x in hex_str])


for line in lines:
    b = hex_to_bin(line)
    print(line)
    print(b)
    left_over, _, _, version_sum, v = process_packet(b)
    print(left_over)
    print(version_sum)
    print(v)
    print()
