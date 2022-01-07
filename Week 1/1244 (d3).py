T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    b, c = map(int, input().split())
    length = 0;
    n = b;
    while n > 0:
        n //= 10
        length += 1

    for i in range(1, c + 1):
        if i > length:
            break
        max_ = 0;
        max_index = 0;
        for j, num in enumerate(str(b)):
            if j < i - 1:
                continue
            if max_ <= int(num):
                max_ = int(num)
                max_index = j

        sumed_num = 0
        saved_num = 0
        for j, num in enumerate(str(b)):
            if j < i - 1:
                curr_num = int(num) * pow(10, length - j - 1)
                sumed_num += curr_num
                continue
            if j == i - 1:
                curr_num = max_ * pow(10, length - j - 1)
                sumed_num += curr_num
                saved_num = int(num)
            elif j == max_index:
                curr_num = saved_num * pow(10, length - j - 1)
                sumed_num += curr_num
            else:
                curr_num = int(num) * pow(10, length - j - 1)
                sumed_num += curr_num
        b = sumed_num

    print(f'#{test_case} {b}')




