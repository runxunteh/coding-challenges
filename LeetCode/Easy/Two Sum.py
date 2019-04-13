"""
https://leetcode.com/problems/two-sum/
Given an array of integers, return indices of the two numbers such that
they add up to a specific target.
Example:
nums=[2,7,11,15]
target=9
nums[0]+nums[1]=2+7=9
return [0,1]
"""

def twosum(nums,target):
    aDict={}
    for i in range(len(nums)):
        complement=target-nums[i]
        if complement in aDict: #if element's complement exist
            return aDict[complement],i #return the two indices
        else:
            aDict[nums[i]]=i    #else add to the dictionary
    return "No two sum solution"

#Test case 1
nums=[2,15,11,7]
target=9
print(twosum(nums,target))
#Test case 2
nums=[2,15,11,8]
target=9
print(twosum(nums,target))
