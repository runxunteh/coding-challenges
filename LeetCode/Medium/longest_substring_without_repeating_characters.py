"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Given a string, find the length of the longest substring without repeating characters.
Example:
Input: "abcabcbb"
Output: 3 (abc)

Input: "bbbbb"
Output: 1 (b)

Input: "pwwkew"
Output: 3 (wke)
"""

def longest_substring(string):
    count=0
    aList=[]

    for i in range(len(string)):
        if string[i] in aList:
            aList=aList[aList.index(string[i])+1:len(aList)]
        aList.append(string[i])
        if len(aList)>count:
            count=len(aList)
    return count

string="pwwkew"
print(longest_substring(string))

