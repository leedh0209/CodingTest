for n in range(0, 10):
    T = int(input())
    a = list(map(int, input().split()))

    loop = True
    while (loop):
        for i in range(1, 6):
            num = a[0]
            a.pop(0)
            num = num - i
            if num <= 0:
                num = 0
                a.append(num)
                loop = False
                break
            else:
                a.append(num)
    print("#{}".format(T), end=" ")
    for i in a:
        print(i, end=" ")
    print()