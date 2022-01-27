import itertools

def find(arr, target):
    result = 0
    for i in range(len(arr)):
        comb = [items for items in itertools.combinations(arr, i) if sum(items) == target]
        result += len(comb)
    return result


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for te in range(1, T + 1):
    a, b = map(int, input().split())
    arr = list(map(int, input().split()))

    result = find(arr, b)
    print(f'#{te} {result}')


