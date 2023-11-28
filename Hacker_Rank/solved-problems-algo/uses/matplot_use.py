from collections import Counter
import matplotlib.pyplot as plt

sales = Counter(banana=15, tomato=66, apple=34, orange=65).most_common()

x, y = zip(*sales)

plt.bar(x,y)

plt.show()

#use this in interactive mode