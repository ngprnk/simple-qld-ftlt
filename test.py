def transform(a):
    if a == 1:
        return a +- 2
    return a

total = 1

for x in [3,5,1]:
    total = total + transform(x)

print(total)

4

