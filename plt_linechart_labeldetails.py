import matplotlib.pyplot as plt
year = [1950,1951, 1952, 2100]
pop = [2.538, 2.57, 2.62,10.85]

plt.plot(year, pop)
plt.xlabel('Year')
plt.ylabel('Population')

plt.title('World Population Projections')

plt.yticks([ 0, 4, 8, 12, 16, 20],['0','4B', '8B', '12B', '16B','20B'])

plt.show()


