T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for te in range(1, 2):
    n = int(input())
    array = [list(map(int, input().split())) for _ in range(n)]


    count = 0
    for i in range(n):
        ready = 0
        for j in range(n):
            if ready == 0 and array[j][i] == 1:
                ready = 1
            elif ready == 1 and array[j][i] == 2:
                count += 1
                ready = 0
    print(f'#{te} {count}')