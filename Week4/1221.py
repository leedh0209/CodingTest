T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for te in range(1, 1 + 1):
    a, b = input().split()
    b = int(b)
    arr = list(input().split())
    arr2 = []

    words = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

    curr = 0
    curr_word = 0

    print(a)
    for i in range(len(words)):
        for j in arr:
            if j == words[curr_word]:
                print(j, end=' ')
        curr_word += 1
    print()

