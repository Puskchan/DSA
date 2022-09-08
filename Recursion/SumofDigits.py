def sumofint(n):
    assert n>=0 and int(n)==n,"num=int and pos"
    if n == 0:
        return 0
    else:
        return int(n%10) + int(sumofint(n//10))
    
print(sumofint(98))