def fac(n):
    assert n>=0 and int(n) == n, "Number should be positive"
    if n in [0,1]:
        return 1
    else:
        return n * fac(n-1)
    
print(fac(5))