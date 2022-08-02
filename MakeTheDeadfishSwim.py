# Author 0x1AE7F (Julian)
# Date: 20th August 2022, 20:54

# Notes:
# Deadfish has 4 commands, each 1 character long:
#
# "i" increments the value (initially 0)
# "d" decrements the value
# "s" squares the value
# "o" outputs the value into the return array


def parse(data: str):
    result_array = []
    buffer = 0
    for letter in data:
        if letter == "i":
            buffer += 1
        elif letter == "d":
            buffer -= 1
        elif letter == "s":
            buffer *= buffer
            pass
        elif letter == "o":
            result_array.append(buffer)
    return result_array