import numpy as np
import time
import sys

'''
l = range(1000)
print(sys.getsizeof(5)*len(l))


array = np.arange(1000)
print(array.size*(array.itemsize))

print(array.size)
print(array.itemsize)
'''

SIZE = 1000000000

# List Processing
l1 = range(SIZE)
l2 = range(SIZE)

start = time.time()
result = [(x+y) for x,y in zip(l1,l2)]
print("List took: ", (time.time()-start)*1000)

# Numpy Processing
n1 = np.arange(1000)
n2 = np.arange(1000)

start = time.time()
result = n1+n2
print("Numpy took: ",(time.time()-start)*1000)
