# Python-Numpy
Python Numpy practices with example
------------------------------------
************************************


Install numpy
	pip install numpy

Calling numpy in program
	import numpy as np


Crating Array
--------------

	Creating numpy single dimension array
		arr = np.array([2,5,3,5,6,4])
		
	Creating multi dimension array
		arr = np.array([[2,5,3,5,6,4],
						[12,15,13,15,16,14],
						[22,25,23,25,26,24]])
	Zeros:
		arr = np.zeros(4)
		arr = np.zeros((2,3))

	Once:
		arr = np.once(4)
		arr = np.once((2,3))
		Output: 
			   [[1 1 1 1 1]
				[1 1 1 1 1]
				[1 1 1 1 1]]

	Empty:						#Return the array with given shape and data type
		arr = np.empty(4)
	
	Eye Function:
		np.eye(4, dtype = int)
		 output:
		 	   [[1 0 0 0]
				[0 1 0 0]
				[0 0 1 0]
				[0 0 0 1]]
							
	Arrange:
		np.arrange(1,11)					#will return 1 to 10
		np.arange(4, 20, 3)					#will return 4 to 19 value with 3 differences
	
	Diagonal:
		arr = np.eye(3)						#Will create 0 and 1 value in diagonal form

	Linspace:
		arr = np.linspace(2,11,num=4)		#Will create array with specifical interval (Start-End-Interval)


Random Functions
----------------
	Random()
		np.random.random(3)					#will return 3 random value in decimal ex. (0212121,0.212121,0.5445)
	
	Rand:
		1D:
			np.random.rand(4)
		2D:
			np.random.rand((2,5))
			
	Randint:
		1D:
			np.random.randint(11,size=(3,3)) 	#will return 3x3 int value
			np.random.randint(2,5,5)
		
	Randn:	can return +ve to -ve
		1D:
			np.random.randn(4)
		
	Randf:	Value from (0.0, 1.0)
		1D:
			np.random.randf(3)
	
Data Type of numpy
-------------------
	Check data type
		arr = np.array([1,2,3,4])
		arr.dtype
	
	Creating array with dtype
		arr = np.array([1,2,3,4], dtype = np.int8)
	
	Converting data type
		new = np.float16(arr)
	
	List of data type:
		bool
		int_									#it cabe int32 or int64
		intc
		intp
		int8
		int16
		int32
		int64
		uint8
		uint16
		uint32
		uint64
		float_
		float16
		float32
		float64
		complex
		complex32
		complex64
	
	Data type as functions
		i - integer
		f - float
		b - boolean
		c - complex
		u - unsigned integer
		M - Date Time
		O - Object
		U - Unicode string
		
		Creating array using special char
			arr = np.array([1,2,3,4],dtype = "f")
	
Arithemetic Operations
-----------------------
	Add/sub/mul/div a numer in array 		#It is change in complete array value
		arr  = np.array([1,2,3,4])
		res  = arr + 2
		res1 = arr - 2
		res2 = arr * 2
		res3 = arr / 2
			
	Add, Sub, Multi, Division with two array
		arr+arr2
		arr-arr2
		arr*arr2
		arr/arr2

	Basic Functions
		np.min(arr)
		np.max(arr)
		np.argmin(arr)
		np.argmax(arr)
		np.sin(arr)
		np.cos(arr)
		np.sqrt(arr)
	
	
Shape and Reshape
------------------
	Shape()
		arr = np.array([[1,2,3],[14,32,65]])
		arr.shape
	
	Converting 1D array to multi Diamention
		arr  = np.array([1,2,3],ndim = 4)
		
	Reshape() 
		arr  = np.array([1,2,3])
		arr.reshape(2, 4)						#Array which is reshaped without changing the data. here 2x4
	Check diamention
		arr.ndim

Indexing and Slicing
---------------------
	Indexing	
 			1D 	- 	[0 1 2 3 4]
			2D	-	[[0,1] 0
					[2,3]] 1
			3D	-	[[[1,2] 0
					  [1,2] 1
					  [2,3]]] 2
			calling arr arr[row, col]
	
	Slicing array
		arr_slicing[Start:Stop:Step]
		arr = np.array[1,2,3,4,5,6,7]
		print(arr[1:5])							#print index 1 to 5
		print(arr[1:])							#print index 1 to last
		print(arr[:5])							#print index 0 to 5
		print(arr[::2])							#print index 0 to last and with 2 interval value
	
	Slicing for 2d array
		arr = np.array([[1,2,3,4] [5,6,7,6] [8,9,7,7]])
							0		 1			2
		arr[1,1:]								#will print [6 7 6]

Iteration functions:
----------------------
	nditer - iterate the array values
		arr = np.array([[1,2,3,4] [5,6,7,6] [8,9,7,7]])
		for i in np.nditer(arr):
			print(i)
	ndenumerate - data and index value
		rr = np.array([[1,2,3,4] [5,6,7,6] [8,9,7,7]])
		for i in np.ndenumerate(arr):
			print(i)

Copy and View Data:
---------------------
	copy function -	Will create new array and copy the data
		arr    = np.array([1,2,3,4])
		arr_cp = arr.copy()
	
	view function - Can view the same data by different reference
		arr    = np.array([1,2,3,4])
		arr_vw = arr.view()
	
Array sorting:
---------------
	np.sort(arr1,axis=1,kind='quicksort')		#will return x axis sorting
	np.sort(arr1,axis=0,kind='quicksort')		#will return y axis sorting

Array Merging:
---------------
	np.vstack((arr, arr2))
	np.hstack((arr,arr2))

Another way merging:
---------------------
	np.concatenate((arr1,arr2),axis=0)			# Y axis merging
	np.concatenate((arr1,arr2),axis=1)			# X axis merging
	
Handling the array with condition:
-----------------------------------
	arr = np.array(arr1)
	arr[arr > 5]						#will return the array vaalue which is greater than 5


Certainly! NumPy is a fundamental library in Python for numerical computations, and it's widely used in Data Science for array manipulation, mathematical operations, and more. Here are some key NumPy topics that are important for Data Science:

Arrays and Basics:

Creating NumPy arrays (using np.array(), np.arange(), np.linspace(), etc.)
Array attributes (shape, size, dimensions)
Indexing and slicing arrays

Array Operations:

Basic arithmetic operations (addition, subtraction, multiplication, division)
Element-wise operations (using broadcasting)
Vectorized operations

Array Manipulation:

Reshaping arrays (using np.reshape(), np.flatten(), np.ravel())
Stacking and splitting arrays
Transposing and swapping axes


Array Broadcasting:

Understanding broadcasting rules
Applying broadcasting for operations on arrays of different shapes
Aggregation and Statistics:

Computing mean, median, variance, and other statistics
Aggregation functions (np.sum(), np.mean(), np.max(), etc.)
Computing along specific axes using axis parameter


Boolean Indexing and Filtering:

Creating boolean masks
Using boolean masks to filter arrays


Array Broadcasting:

Understanding broadcasting rules
Applying broadcasting for operations on arrays of different shapes
Mathematical Functions:

Trigonometric functions (np.sin(), np.cos(), np.tan())
Exponential and logarithmic functions
Linear algebra operations (np.dot(), np.linalg.inv(), np.linalg.eig())
Random Number Generation:

Generating random numbers and arrays
Distributions (uniform, normal, etc.)
Array Comparison and Sorting:

Element-wise comparisons (greater than, less than, equal to)
Sorting arrays (np.sort(), np.argsort())
Array Broadcasting:

Understanding broadcasting rules
Applying broadcasting for operations on arrays of different shapes
Masked Arrays:

Dealing with missing or invalid data using masked arrays
File Input/Output:

Reading and writing arrays from/to files (CSV, binary, etc.)
Advanced Indexing:

Fancy indexing using arrays of indices
Boolean indexing with multiple conditions
Universal Functions (ufuncs):

Applying functions element-wise to arrays
Using np.vectorize() for custom functions
NumPy is a versatile library, and these topics cover the basics you'll need to work effectively with arrays and perform numerical computations in the context of Data Science.
