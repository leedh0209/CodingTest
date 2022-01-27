T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for te in range(1, T + 1):
    a = int(input())
    arr = str(input())
    s = ['' for _ in range(len(arr))]

    for i in range(len(arr)):
        s[i] = arr[i:]
    s.sort()

    print(f'#{te} {s[a-1]}')

