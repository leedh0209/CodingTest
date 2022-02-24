import math
"""
def more_dist(x, weight, d, curr):
    newd = d
    for i in range(curr + 2, len(x)):
        newd = math.sqrt(newd / weight[i])
        print('test1')
    for i in range(curr - 1, -1, -1):
        newd = math.sqrt(newd / weight[i])
        print('test2')
    return newd
"""

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for te in range(1, T + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    x = arr[0:n]
    weight = arr[n:n * 2]

    result = '#' + str(te) + ' '
    for i in range(n - 1):
        xt = x[i + 1] - x[i]
        a = math.sqrt(weight[i] / weight[i + 1])
        d = xt / (a + 1)
        #reald = more_dist(x, weight, d, i)
        result += '{:.10f} '.format(x[i+1]-d)
    print(result)

#멘탈 나가버려서 못하겠음 ㅋㅋㅋㅋ