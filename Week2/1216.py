def count(startCol, startRow, endCol, endRow, list1, array):
    length = len(list1)
    if startCol == endCol:
        while list1 == list(reversed(list1)) and startRow > 0 and endRow < 99:
            startRow -= 1
            endRow += 1
            list1.insert(0, array[startCol][startRow])
            list1.append(array[endCol][endRow])
            if list1 == list(reversed(list1)):
                length += 2
    elif startRow == endRow:
        while list1 == list(reversed(list1)) and startCol > 0 and endCol < 99:
            startCol -= 1
            endCol += 1
            list1.insert(0, array[startCol][startRow])
            list1.append(array[endCol][endRow])
            if list1 == list(reversed(list1)):
                length += 2
    return length


T = 10

for te in range(1, 2):
    n = int(input())
    array = [list(str(input())) for _ in range(100)]

    max_len = 0

    for i in range(100):
        list1 = []
        for j in range(100):
            list1.append(array[i][j])
            if j >= 14:
                if list1 == list(reversed(list1)):
                    leng = count(i, j - 14, i, j, list1, array)
                    if leng > max_len:
                        max_len = leng
                list1.pop(0)
    for i in range(100):
        list1 = []
        for j in range(100):
            list1.append(array[i][j])
            if j >= 15:
                if list1 == list(reversed(list1)):
                    leng = count(i, j - 15, i, j, list1, array)
                    if leng > max_len:
                        max_len = leng
                list1.pop(0)

    for i in range(100):
        list1 = []
        for j in range(100):
            list1.append(array[j][i])
            if j >= 14:
                if list1 == list(reversed(list1)):
                    leng = count(j - 14, i, j, i, list1, array)
                    if leng > max_len:
                        max_len = leng
                list1.pop(0)
    for i in range(100):
        list1 = []
        for j in range(100):
            list1.append(array[j][i])
            if j >= 15:
                if list1 == list(reversed(list1)):
                    leng = count(j - 15, i, j, i, list1, array)
                    if leng > max_len:
                        max_len = leng
                list1.pop(0)

    print(f'#{te} {max_len}')