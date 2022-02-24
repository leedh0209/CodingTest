def cutsquare(bigsquare, arr, curr):
    x = 0
    y = 0
    while x < len(bigsquare) and y < len(bigsquare):
        if bigsquare[x][y] == 0:
            if check(bigsquare, pow(2, arr[curr]), x, y):
                mark_square(bigsquare, pow(2, arr[curr]), x, y)
                return 1
            else:
                x = 0
                y += pow(2, arr[curr])
        if x == len(bigsquare) - 1:
            x = 0
            y += 1
        x += 1
    return 0

def check(bigsquare, need, x, y):
    if x + need - 1 < len(bigsquare) and y + need - 1 < len(bigsquare):
        if bigsquare[x][y] == 0 and bigsquare[x + need - 1][y] == 0 and bigsquare[x][y + need - 1] == 0 and \
                bigsquare[x + need - 1][y + need - 1] == 0:
            return 1
        else:
            return 0
    else:
        return 0

def mark_square(bigsquare, need, x, y):
    for i in range(need):
        bigsquare[x+i][y:y+need] = [1 for _ in range(need)]

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for te in range(1, T + 1):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    arr_visited = [0 for _ in range(n)]

    bigsquare = [[0 for _ in range(m)] for _ in range(m)]
    curr = 0
    total = 0
    while 0 in arr_visited:
        if arr_visited[curr] == 0:
            if cutsquare(bigsquare, arr, curr):
                arr_visited[curr] = 1
        curr += 1
        if curr >= len(arr):
            bigsquare = [[0 for _ in range(m)] for _ in range(m)]
            curr = 0
            total += 1

    print(f'#{te} {total}')
    
'메모리 초과로 x같이 멸망 ㅠㅠㅠ'