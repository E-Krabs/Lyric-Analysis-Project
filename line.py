import matplotlib.pyplot as plt
   
year = [2017, 2018, 2019, 2020]
love = [267, 212, 240, 180]
oh = [373, 184, 234, 238]

plt.plot(year, love, color='red', marker='o', label='love')
plt.plot(year, oh, marker='o', label='oh')

plt.title('Love Trend (2017-2020)')
plt.xlabel('Year')
plt.ylabel('Count')
plt.grid()
plt.legend()
plt.show()