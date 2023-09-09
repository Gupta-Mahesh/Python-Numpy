
"""In this file covering the random funtion"""

import numpy as np

rand_num1 = np.random.random(3)
print("Random.random(3):\n",rand_num1)

"""np.random.rand
   This function takes a tuple to specify the size of the output
"""

#1d array by rand
rand_num2 = np.random.rand(3)
print("Random.rand(3):\n",rand_num2)

#2d array by rand
rand_num3 = np.random.rand(2,5)
print("Random.rand(2,5):\n",rand_num3)

"""
Randint: Return random integers from low (inclusive) to high (exclusive).
			random.randint(low, high=None, size=None, dtype=int)
            """

rand_num4 = np.random.randint(11,21,size=(3,5),dtype=int)
print("Random.randint(11,21,size=(3,5),dtype=int):\n",rand_num4)

rand_num5 = np.random.randint(1,11,5)
print("Random.randint(1,11,5):\n",rand_num5)

rand_num6 = np.random.randn(4)
print("Random.rand(4):\n",rand_num6)

rand_num7 = np.random.ranf(5)
print("random.ranf(5):\n",rand_num7)