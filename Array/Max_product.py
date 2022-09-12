import numpy as np

arr = np.array([1,15,9,18,4,3,27,6,11,19,6,21,12])

prod = 0

for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i]*arr[j] > prod:
            prod = arr[i]*arr[j]

print(prod)
            