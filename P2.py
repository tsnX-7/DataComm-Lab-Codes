# 2. Determine the even parity codeword of a dataword.
# Highlight the parity added.
# Determine if a codeword is corrupted using parity checking.

def generate_codeword():
    dataword = input('Enter the dataword: ')
    parity_bit = (dataword.count('1')+0)%2  #for even-parity, add 0 before modulo 2
                                            #for odd-parity, add 1 before modulo 2
    print('The parity bit:', parity_bit)
    codeword = dataword + str(parity_bit)
    print('The codeword is:', codeword)

def check_codeword():
    codeword = input('Enter codeword: ')
    parity_bit = int(codeword[len(codeword)-1])
    dataword = codeword[:len(codeword)-1]
    print(dataword)
    temp_parity_bit = (dataword.count('1')+0)%2
    print(temp_parity_bit, parity_bit)
    if temp_parity_bit == parity_bit:
        print('Yaay! Codeword was correctly generated!')
    else:
        print('Ooops! Codeword is corrupted!')

print('1. Generate Codeword using parity-bit')
print('2. Check the codeword for parity-bit')
choice = int(input('Choose a type: '))
if choice==1:
    generate_codeword()
else:
    check_codeword()