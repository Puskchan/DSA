def power(x, n):
    assert n>0 and int(n)==n, "number and expo should be positive"
    if n in [0,1]:
        return 1
    else:
        return x * power(x , (n-1))

print(power(2, -9))