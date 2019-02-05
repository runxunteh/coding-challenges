"""
A method to replace all spaces in a string with "%20"
Assume the string has sufficient space at the end to hold the additional characters
Assume we are given the "true" length of the string
Example:
Input: "Mr John Smith    ", 13(true length)
Output: "Mr%20John%20Smith"
If don't assume the string has sufficient space at the end:
we need trueLength+spacecount+2
Example:
Input: "Mr John Smith", 13
so we have two spaces in the string, we will need an additional of 4 spaces at the end
"""

def urlify(str,true_length):
    char_list=list(str)
    index=len(str)
    for i in range(true_length-1, -1, -1):
        if str[i]==" ":
            char_list[index-1]="0"
            char_list[index-2]="2"
            char_list[index-3]="%"
            index-=3
        else:
            char_list[index-1]=str[i]
            index-=1
    return "".join(char_list)

str="Mr John Smith    "
true_length=13
print(urlify(str,true_length))
