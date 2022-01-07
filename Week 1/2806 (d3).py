import copy

T = int(input())

#testcase function에서는 start위치(y = 0) 에서 각 x에 대한 for문으로 시작
#array도 global로 잡고 해야 함
#현재 위치에서 위 3방향으로 움직이면서 queen이 있는지 확인해야 함
#만약 움직이는 과정에서 queen이 발견되지 않았다면
#현재 위치를 표기하고 다음 함수를 부른다음(y + 1) 다시 현재 위치를 지움

def nq(y, x, rest, array):
    global answer
    if (x < 0 or y < 0 or x >= len(array) or y >= len(array)):
        return
    if array[x][y] == 1:
        return
    if rest <= 0:
        answer += 1
        return

    for j in range(len(array)):
        array2 = copy.deepcopy(array)

        for x2 in range(len(array)):
            for y2 in range(y, len(array)):
                if (x2 == x or y2 == y or (x + y) == (x2 + y2) or (x - y) == (x2 - y2)):
                    array2[x2][y2] = 1
        for n in range(len(array)):
            nq(y + 1, n, a - 1, array2)
    return


# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    a = int(input())
    answer = 0
    array = [[0] * a for i in range(a)]

    for i in range(a):
        if (a == 1):
            answer = 1
            break

        array2 = copy.deepcopy(array)

        for x in range(len(array)):
            for y in range(len(array)):
                if (x == 0 or y == i or i == (x + y) or i == (x - y)):
                    array2[x][y] = 1
        print(array2)
        for j in range(a):
            nq(1, j, a - 1, array2)

    print(f'#{test_case} {answer}')