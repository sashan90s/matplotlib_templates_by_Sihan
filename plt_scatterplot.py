import matplotlib.pyplot as plt
import numpy as np
year = [1950,1951, 1952, 2100]
pop = [2.538, 2.57, 2.62,10.85]
'''we need to double the pop because we want to correspond country
with size
beng: country er popuplation size
joto boro hobe, amar dots o toto boro hobe'''
double_pop = np.array(pop) * 2
''' 
s =  here is defining the size of the scartter
dots
'''

# alpha means transparency, c means color,s means size of dots
# you can either create a list of colors to match the x and y axis data points
# or, you can give one color hard coded for all the points.
plt.scatter(year, pop, s=double_pop, c= ['red', 'green', 'blue', 'yellow'], alpha = 0.9)
plt.xlabel('Year')
plt.ylabel('Population')

plt.title('World Population Projections')

# this will help assign names to ticks on y axis
plt.yticks([ 0, 4, 8, 12, 16, 20],['0','4B', '8B', '12B', '16B','20B'])
# this will print name of the country next to the dot.
plt.text(1950, 2.538, 'Bangladesh')
plt.grid(True) # this will add grid line
plt.show()