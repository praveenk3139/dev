import numpy as np

arr = np.array([1, 2, 3, 4, 5])
sub_arr = arr[1:4]

# Operations & Math
print("Array:", arr)
print("Mean & Sum:", arr.mean(), arr.sum())
print("Sqrt & Exp:", np.sqrt(arr), np.exp(arr))
print("First & Slice:", arr[0], sub_arr)
print("Concatenated:", np.concatenate([arr, sub_arr]))