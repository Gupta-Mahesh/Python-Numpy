import numpy as np

# Ndim Function
    #numpy.ndarray.ndim() function return the number of dimensions of an array.

arr1 = np.array([1,2,3,1,2,3])
arr2 = np.array([[1,2,3],[1,2,3]])

print(arr1.ndim)
print(arr2.ndim)

arr3 = np.array(arr1, ndmin = 3)
print("ndim array:\n",arr3.ndim)

# Zeros Function
    # The numpy.zeros() function returns a new array of given shape and type, with zeros. Syntax:
    #numpy.zeros(shape, dtype = None)

arr = np.zeros(shape = (3,5), dtype = int)
print("Zero function:\n",arr)

# Ones Function
    # The numpy.ones() function returns a new array of given shape and type, with ones.
    #Syntax: numpy.ones(shape, dtype = None)

arr = np.ones(shape = (3,5), dtype = int)
print("Once Function:\n",arr)

# Eye Function
    # The eye tool returns a 2-D array with 1’s as the diagonal and 0’s elsewhere. The diagonal can be main, upper, or lower depending on the optional parameter k.

print("Eye Function:\n",np.eye(4, dtype = int))

# Empty Function
    # Return am empty array of given shape and type

print("Empty Function:\n",np.empty(shape=(4,5), dtype=int, order="C"))

""" [[4128860 6029375 3801188 5636188 7536745]
    [6357109 2097260 7602259 6553717 7274601]
    [5701664 7471215 5439595 6357104 6619235]
    [5242972 7602297 7274600 6226030 7667790]] 
"""