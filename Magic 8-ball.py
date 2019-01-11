#https://www.pythonforbeginners.com/code-snippets-source-code/magic-8-ball-written-in-python/

import random

question=input("Ask the magic 8 ball a question: ")
ans=random.randint(0,7)
aList=["It is certain","Outlook good","You may rely on it","Ask again later","Concentrate and ask again","Reply hazy, try again","My reply is no","My sources say no"]
print(aList[ans])
