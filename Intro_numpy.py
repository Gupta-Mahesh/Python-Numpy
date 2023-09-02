"""Installed Numpy using --> pip install numpy"""

import numpy as np

arr = np.array([2,3,4,5,6])
arr2 = np.array([21,31,44,35,56])

print("Two Array Sum:\n",arr+arr2)

arr3=np.array([[12,32,55,44],
              [52,56,54,55]])
print("Nd Array: \n",arr3)

arr3.shape = (4,2)
print("Reshaping to 4x2:\n",arr3)

arr4=np.arange(27)
print("\narange():\n",arr4)

mn = arr4.reshape(3,3,3)
print("\nReshape:\n",mn)

linspace =np.linspace(2,6,10,retstep=True)   #Start 2 -End 6 -Times 10 -DifferenceValue 
print("\nLinspace:\n",linspace)

randon_int=np.random.randint(5,size=(5,5))
print("\nRandom Int:\n",randon_int)

