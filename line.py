import matplotlib.pyplot as plt
   
year = [2017, 2018, 2019, 2020]
x = []
y = []

plt.plot(year, x, color='red', marker='o', label='x')
plt.plot(year, y, marker='o', label='y')

plt.title('TITLE')
plt.xlabel('Year')
plt.ylabel('Count')
plt.grid()
plt.legend()
plt.show()
