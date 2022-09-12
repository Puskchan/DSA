def ts(arr, n):
    s = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == n and arr[i] != arr[j]:
                s += 1
                print(f'({i},{j})')

ts([1,2,3,4], 5)