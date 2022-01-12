def find_path(curr, dic1, dic2):
    global result
    if curr in dic1:

        if dic1[curr] == 99:

            result = 1
        elif curr in dic2:
            if dic2[curr] == 99:

                result = 1
            else:
                find_path(dic1[curr], dic1, dic2)
                find_path(dic2[curr], dic1, dic2)
        else:
            find_path(dic1[curr], dic1, dic2)
    else:
        return


T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for te in range(1, 2):
    n, len = map(int, input().split())
    arr = list(map(int, input().split()))

    dic1 = {}
    dic2 = {}
    for i in range(0, len*2, 2):
        if arr[i] not in dic1:
            dic1[arr[i]] = arr[i + 1]
        else:
            dic2[arr[i]] = arr[i + 1]

    result = 0
    find_path(0, dic1, dic2)
    print(f'#{te} {result}')

