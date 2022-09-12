def fno(arr, n):
    for i in range(len(arr)):
        if arr[i] == n:
            return i


print(fno([1,2,3,4,5], 5))