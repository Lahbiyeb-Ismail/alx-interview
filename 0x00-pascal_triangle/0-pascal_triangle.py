#!/usr/bin/python3


def pascal_triangle(n):
    result = [[1]]

    for _ in range(n - 1):
        tempList = [0] + result[-1] + [0]
        newRow = []
        for j in range(len(result[-1]) + 1):
            newRow.append(tempList[j] + tempList[j + 1])

        result.append(newRow)

    return result
