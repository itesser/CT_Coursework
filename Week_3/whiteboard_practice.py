# Given a rectangular matrix of characters, add a border of asterisks(*) to it.

# Example

# For

# picture = ["abc",
#            "ded"]
# the output should be

# solution(picture) = ["*****",
#                      "*abc*",
#                      "*ded*",
#                      "*****"]
# Input/Output


def draw_border(input_array):
    result = []
    border = "*" * (len(input_array[1]) + 2)
    result.append(border)
    for i in range(len(input_array)):
        result.append("*" + input_array[i] + "*")
    result.append(border)
    return result


result = draw_border(["abcge", "dared", "rsabr"])

for i in result:
    print(i)
