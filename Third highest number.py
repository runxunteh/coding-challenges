#A program that reads ten numbers and figures out which number is the third highest

aList=[5,4,2,1,3,8,9,6,7,10]
no1=0
no2=0
no3=0

for i in range(len(aList)):
    if aList[i]>no1:
        if no1>no2:
            no3=no2
            no2=no1
        no1=aList[i]
    elif aList[i]>no2:
        no2=aList[i]
    elif aList[i]>no3:
        no3=aList[i]

print(no3)
    
