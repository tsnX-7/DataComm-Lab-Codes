# 4. Determine the Checksum codeword for a list of five 8-bit numbers

nums = []
bit_len = int(input('Enter bit length: '))
for _ in range(5):
    nums.append(int(input()))
sum = sum(x for x in nums)
sum_bin = bin(sum)[2:]
wrapped_sum = sum

if(len(sum_bin) > bit_len):
    wrapped_sum = int(sum_bin[-bit_len:],2) + int(sum_bin[:-bit_len],2)
check_sum = wrapped_sum ^ ((1<<bit_len)-1)

print('The check sum is:', check_sum)



'''
4
7
11
12
0
6
ans: 9


8
7
11
12
0
6
ans: 219 (11011011, complement of 36(00100100))
'''