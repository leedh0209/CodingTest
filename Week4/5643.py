def is_contain(lst, c):
    for i in lst:
        if c in i:
            return 1
    return 0


def find_loc(lst, c):
    for i in range(len(lst)):
        if c in lst[i]:
            return i
    return -1

def find_all_loc(lst, c):
    loc_lst = []
    for i in range(len(lst)):
        if c in lst[i]:
            loc_lst.append(i)
    return loc_lst


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for te in range(1, T + 1):
    n = int(input())
    m = int(input())
    arr = [list(map(int, input().split())) for _ in range(m)]
    visited = [0 for _ in range(m)]
    lst = []

    lst.append([arr[0][0]])
    lst.append([arr[0][1]])
    visited[0] = 1
    i = 1
    while i < len(arr):
        if is_contain(lst, arr[i][0]):
            if not is_contain(lst, arr[i][1]):
                visited[i] = 1
                loc = find_loc(lst, arr[i][0])
                if loc == len(lst) - 1:
                    lst.append([arr[i][1]])
                else:
                    for j in range(loc + 1, len(lst)):
                        lst[j].append(arr[i][1])
            else:
                visited[i] = 1
                locs1 = find_all_loc(lst, arr[i][0])
                locs2 = find_all_loc(lst, arr[i][1])
                if len(set.intersection(set(locs1), set(locs2))) > 0:
                    for j in range(0, max(locs1)):
                        if arr[i][1] in lst[j]:
                            lst[j].remove(arr[i][1])
                    for j in range(min(locs2), len(lst)):
                        if arr[i][0] in lst[j]:
                            lst[j].remove(arr[i][0])
        else:
            if is_contain(lst, arr[i][1]):
                visited[i] = 1
                loc = find_loc(lst, arr[i][1])
                if loc == 0:
                    lst.insert(0, [arr[i][0]])
                else:
                    for j in range(0, loc):
                        lst[j].append(arr[i][0])
        i += 1
        if i == len(arr):
            if 0 in visited:
                i = 1

    total = 0
    for i in lst:
        if len(i) == 1:
            total += 1
    print(f'#{te} {total}')

#아직 못품품

