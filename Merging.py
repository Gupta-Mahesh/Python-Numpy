
import numpy as np

arr1 = np.array([[20,13,43,5,6],
                [21,31,44,35,56],
                [1,30,20,30,50]])
arr2 = np.array([[201,131,431,51,61],
                [212,312,442,352,562],
                [13,303,203,303,503]])

arr_merg_v = np.vstack((arr1,arr2))
print(arr_merg_v)

arr_merg_h = np.hstack((arr1,arr2))
print(arr_merg_h)

arr_concat_y =np.concatenate((arr1,arr2),axis=0)
print("Y Axis Concatination:\n",arr_concat_y)

arr_concat_x =np.concatenate((arr1,arr2),axis=1)
print("X Axis Concatination:\n",arr_concat_x)

print(np.vsplit(arr1,3))


#Array Slicing

arr_slicing = np.array([1,2,3,4,5,6,7,8])
print(arr_slicing[3:])
print(arr_slicing[3:-3])

arr_2d_slicing = np.array([[1,2,3,4],
                           [5,6,7,8],
                           [8,7,6,5],
                           [4,3,2,1]])

print("2D slicing\n",arr_2d_slicing[ 1:2 , 1:2])   #[row, col]

print("2D slicing\n",arr_2d_slicing[ 2:3 , 1:2])   #[row, col]

#checking with condition in np array
arr_automatic = [1,2,3,1,4,4,7,7,8,7,8,77,88,5,44,55]
np_arr_auto = np.array(arr_automatic)

print(len(np_arr_auto[np_arr_auto > 5]))

print(np_arr_auto[np_arr_auto > 5])
