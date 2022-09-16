def rot(arr):
    n = len(arr)
    for la in range(n//2):
        f = la
        l = n - la - 1
        for i in range(f,l):
            top = arr[la][i]
            arr[la][i] = arr[-i-1][la]
            arr[-i-1][la] = arr[-la-1][-i-1]
            arr[-la-1][-i-1] = arr[i][-la-1]
            arr[i][-la-1] = top
    return arr

arr = [[1,2,3],
       [4,5,6],
       [7,8,9]]

print(rot(arr))