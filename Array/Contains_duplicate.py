l = [1,2,3,4,5,6,2,7,8,9]
a = []

for i in l:
    if i not in a:
        a.append(i)

print(len(l)>len(a))