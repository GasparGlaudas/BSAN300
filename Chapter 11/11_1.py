""" 
While our implementations (stats.py) work correctly on data set of numbers, they are not necessarely 
the best versions to use with very large data sets. They are too slow for big data databases. 
To mitigate these problems, you can import some of the functions with Numpy, a popular library for numerical analysis, 
which is better than the stat module  
"""

import numpy as np

lyst = [1, 2, 3, 4]
print(np.mean(lyst))
print(np.median(lyst))
print(np.std(lyst))

