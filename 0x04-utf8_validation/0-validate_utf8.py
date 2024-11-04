#!/usr/bin/python3
"""
UTF-8 Encoding Validation
"""


def validUTF8(data):
    """
    Implementation
    """
    point = 0
    while point < len(data):
        Byte1 = data[point] & 255
        if not Byte1 >> 7:
            point += 1
            continue
        elif (Byte1 >> 5) == 6:
            try:
                Byte2 = data[point + 1]
                if (Byte2 >> 6) == 2:
                    point += 2
                    continue
                else:
                    return False
            except IndexError:
                return False
        elif (Byte1 >> 4) == 14:
            try:
                Byte2 = data[point + 1]
                Byte3 = data[point + 2]
                if (Byte2 >> 6) == (Byte3 >> 6) == 2:
                    point += 3
                    continue
                else:
                    return False
            except IndexError:
                return False
        elif (Byte1 >> 3) == 30:
            try:
                Byte2 = data[point + 1]
                Byte3 = data[point + 2]
                Byte4 = data[point + 3]
                if (Byte2 >> 6) == (Byte3 >> 6) == (Byte4 >> 6) == 2:
                    point += 4
                    continue
                else:
                    return False
            except IndexError:
                return False
        else:
            return False
    return True