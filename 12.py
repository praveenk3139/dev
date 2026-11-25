import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 30, 25]
plt.plot(x, y)
plt.title("Line Plot")
plt.show()
plt.bar(x, y)
plt.title("Bar Chart")
plt.show()
plt.scatter(x, y)
plt.title("Scatter Plot")
plt.show()
plt.hist(y, bins=5)
plt.title("Histogram")
plt.show()
plt.pie(y, labels=x, autopct='%1.1f%%')
plt.title("Pie Chart")
plt.show()