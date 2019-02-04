#Given two strings, write a method to decide if one is a permutation of the other

def permutation(s,t):
    if len(s)!=len(t):
        return False
    else:
        s_array=[0]*128
        for i in range(len(s)):
            index=ord(s[i])-97
            s_array[index]+=1
        for i in range(len(t)):
            index=ord(t[i])-97
            s_array[index]-=1
            if s_array[index]<0:
                return False
        return True

s="dog"
t="god"
print(permutation(s,t))
