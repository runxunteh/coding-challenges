#An algorithm to determine if a string has all unique characters

def isUniqueChars(str):
    checker=0
    for i in range(len(str)):
        val=ord(str[i])-97
        #&: bitwise AND
        #<<: left shift. x<<y: multiplying x with 2^y. E.g. val=2. 1<<2=1*(2^2)=4
        if (checker & (1<<val)) >0:
            return False
        else:
            checker+=(1<<val)
    return True

print(isUniqueChars("aba"))
