import numpy as np

arr1 = np.array([[20,13,43,5,6],
                [21,31,44,35,56],
                [1,30,20,30,50]])


# row wise sorting 
print("Row-Wise sorting:\n", np.sort(arr1,axis=1,kind='quicksort'))

# column wise sorting
print("\nColumn-Wise sorting:\n",np.sort(arr1,axis=0,kind='quicksort'))

# Default sorting without axis value
print("\nDefault sorting:\n",np.sort(arr1,kind='quicksort'))
