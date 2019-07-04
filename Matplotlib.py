#Reference: https://towardsdatascience.com/matplotlib-tutorial-learn-basics-of-pythons-powerful-plotting-library-b5d1b8f67596

import matplotlib.pyplot as plt

#Solid blue line
plt.subplot(1,2,1)
plt.plot([1,6],[0,6])
plt.title("Straight Line")
plt.xlabel("x-label")
plt.ylabel("y-label")

#Green circles
plt.subplot(1,2,2)
plt.plot([1,6],[0,6],"go")
plt.title("Straight Line")
plt.xlabel("x-label")
plt.ylabel("y-label")
plt.suptitle("Subplots")
plt.show()

#Pie chart
company=["Company A", "Company B"]
percentage=[70,30]
Explode=[0,0.1]
plt.pie(percentage,explode=Explode,labels=company)
plt.axis("equal")
plt.legend(title="Company")
plt.show()
