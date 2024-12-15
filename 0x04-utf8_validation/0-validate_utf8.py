#!/usr/bin/python3
'''
A module to determine if a data s
'''


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    :param data: List of integers representing bytes of data
    :return: True if data is a valid UTF-8 encoding, else False
    """
    i = 0
    while i < len(data):
        byte = data[i]

        # 1-byte sequence: 0xxxxxxx
        if byte & 0b10000000 == 0:
            i += 1
            continue

        # Determine the number of bytes in the sequence
        num_bytes = 0
        if byte & 0b11100000 == 0b11000000:  # 2-byte sequence: 110xxxxx
            num_bytes = 2
        elif byte & 0b11110000 == 0b11100000:  # 3-byte sequence: 1110xxxx
            num_bytes = 3
        elif byte & 0b11111000 == 0b11110000:  # 4-byte sequence: 11110xxx
            num_bytes = 4
        else:
            return False

        # Check continuation bytes
        for j in range(1, num_bytes):
            if i + j >= len(data) or data[i + j] & 0b11000000 != 0b10000000:
                return False

        i += num_bytes

    return True
