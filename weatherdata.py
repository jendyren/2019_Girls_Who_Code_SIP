#import weather
#list_of_report = weather.get_weather()

import matplotlib.pyplot as plt

population_ages = [2, 7, 12, 15, 5, 6, 1, 1]

bins = [10, 20, 30, 40, 50, 60, 70, 80]

plt.hist(population_ages, bins, histtype='bar', rwidth=0.8)

plt.xlabel('Temperature')
plt.ylabel('Number of cities')
plt.title('Average Temperature\nJanuary 2016')
plt.legend()
plt.show()
