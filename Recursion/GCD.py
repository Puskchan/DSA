def GCD(x,y):
    assert int(x)==x and int(y)==y, "Num = int"
    if x < 0:
        x = -1 * x
    if y < 0:
        y = -1 * y
    if y == 0:
        return x
    else:
        return GCD(y, x%y)


print(GCD(48,18))