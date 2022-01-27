T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for te in range(1, T + 1):
    arr = list(str(input()))

    curr = 0
    num = 0
    index = 0
    total = [0]
    while curr < len(arr):
        if arr[curr] == '(':
            if arr[curr + 1] == ')':
                total[index] += num
                curr += 2
                index += 1
                total.append(0)
            else:
                num += 1
                curr += 1
        else:
            total[index] += 1
            curr += 1
            index += 1
            num -= 1
            total.append(0)

    print(f'#{te} {sum(total)}')
