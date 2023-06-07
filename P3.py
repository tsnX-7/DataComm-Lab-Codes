# 3. Determine the CRC codeword for a given a dataword and a divisor.
# Determine if the codeword is corrupted using CRC checker.

def generate_CRC_codeword():
    dataword = input('Enter the dataword: ')
    divisor = input('Enter the divisor: ')
    len_rem = len(divisor)-1
    dividend = dataword + ''.join('0' for _ in range(len_rem))
    print(dataword, divisor, dividend)

    rem = dividend[:len_rem]
    for i in range(len_rem, len(dividend)):
        rem += dividend[i]
        if rem[0] != '0':
            temp = ''
            for x, y in zip(rem, divisor):
                temp += str(int((x!=y)))
            rem = temp
        rem = rem[1:len(rem)]

    codeword = dataword + rem
    print('The remainder is:', rem)
    print('The codeword is:', codeword)

def CRC_checker():
    codeword = input('Enter the codeword: ')
    divisor = input('Enter the divisor: ')
    len_rem = len(divisor)-1
    dividend = codeword
    expected_rem = ''.join('0' for _ in range(len_rem))

    rem = dividend[:len_rem]
    for i in range(len_rem, len(dividend)):
        rem += dividend[i]
        if rem[0] != '0':
            temp = ''
            for x, y in zip(rem, divisor):
                temp += str(int((x != y)))
            rem = temp
        rem = rem[1:len(rem)]

    if(rem == expected_rem):
        print('CRC was generated successfully!')
    else:
        print('Ooops! CRC codeword corrupted!')


print('1. Generate Codeword using CRC')
print('2. Check the codeword for CRC')
choice = int(input('Choose a type: '))
if choice==1:
    generate_CRC_codeword()
else:
    CRC_checker()


'''
1001
1011
'''

'''
1001110
1011
'''