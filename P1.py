# 1. Determine the minimum hamming distance in a set of codewords.

n = int(input('Enter number of codewords: '))

codewords = []
codewords = [input() for _ in range(n)]

dis = []
for i in range(n):
    for j in range(i+1, n):
        cnt = 0
        for x, y in zip(codewords[i], codewords[j]):
            cnt += int(x!=y)
        dis.append(cnt)

print('Minimum hamming distance in the set of given codewords: ', min(dis))



'''
4
00000
01011
10101
11110

Output:
Minimum hamming distance of the given codewords:  3
'''


