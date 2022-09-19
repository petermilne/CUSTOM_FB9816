#!/usr/bin/env python3

OFFSET=0x1000


for ch in range(1,33):
    print("m{:02d} 0x{:04x} 0x{:08x} rw %08x".format(ch, OFFSET, 0xffffffff))
    OFFSET += 4
    print("c{:02d} 0x{:04x} 0x{:08x} rw %08x".format(ch, OFFSET, 0xffffffff))
    OFFSET += 4


