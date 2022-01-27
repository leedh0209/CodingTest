T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for te in range(1, T + 1):
    arr = list(str(input()))

    list_ = []
    broken = 0
    for i in arr:
        if i not in list_:
            list_.append(i)
        if i in list_:
            if list_.count(i) > 2:
                print(f'#{te} No')
                broken = 1
                break
            else:
                list_.append(i)
    if len(set(list_)) == 2 and broken == 0:
        print(f'#{te} Yes')
    elif len(set(list_)) != 2 and broken == 0:
        print(f'#{te} No')