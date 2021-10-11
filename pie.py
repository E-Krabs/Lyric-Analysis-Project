import matplotlib.pyplot as plt
import numpy as np

y = np.array([899, 817, 750, 745])
mylabels = ["love", "oh", "god", "you're"]
myexplode = [0.2, 0, 0, 0]

plt.pie(y, labels = mylabels, explode=myexplode, autopct='%1.2f%%')
plt.show() 