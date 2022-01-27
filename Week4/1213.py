T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for te in range(1, T + 1):
    n = int(input())
    search = str(input())
    string = str(input())

    total = 0
    curr = 0
    while 1:
        loc = string[curr:].find(search)
        if loc == -1:
            break
        else:
            total += 1
            curr = curr + loc + len(search)
    print(f'#{te} {total}')