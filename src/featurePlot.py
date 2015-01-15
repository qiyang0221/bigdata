import matplotlib
import matplotlib.pyplot as plt
from numpy import *

def draw(dictionary,feature):
   y = zeros(len(dictionary))
   i = 0
   for key in dictionary.keys():
       y[i] = dictionary[key][feature]
       i += 1
   
   x = range(len(dictionary))

   plt.plot(x,y)
   plt.xlabel("student")
   plt.ylabel(feature)
   plt.title(feature)
   plt.show()
