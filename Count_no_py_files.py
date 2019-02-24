import os
count=0
for root, dirs, files in os.walk("."):  
    for filename in files:
        if filename.endswith(".py"):
            print(filename)
            count+=1
print(count-1) #counting file(this file) not counted
