T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for te in range(1, T + 1):
    a, b = map(int, input().split())
    axy = [1, 1]
    bxy = [1, 1]

    curr = 1
    total = 1
    while a > total:
        curr += 1
        total += curr
    dis = total - a
    axy[0] = 1 + dis
    axy[1] = curr - dis

    curr = 1
    total = 1
    while b > total:
        curr += 1
        total += curr
    dis = total - b
    bxy[0] = 1 + dis
    bxy[1] = curr - dis

    new = [axy[0] + bxy[0], axy[1] + bxy[1]]

    newResult = 1
    for i in range(1, new[0] + new[1] - 1):
        newResult += i
    print(f'#{te} {newResult + new[1] - 1}')