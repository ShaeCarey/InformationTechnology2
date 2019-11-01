import matplotlib.pyplot as plt

xlist = [1,2,3,4,5,6,7,8,9,10]
ylist = ['Harry','jo','alexa','sam','gavin','keith','kev','jake','sam','bela']

plt.xlabel("This is X")
plt.ylabel("This is Y")

plt.title("This is my plot!")

plt.pie(xlist)

plt.show()