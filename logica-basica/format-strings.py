a = 'A'
b = 'B'
c = 1.1
string = 'a={name1} b={name2} c={name3:.2f} d={name3:.2f}'
format = string.format(
    name1 = a, name2 = b, name3 = c
)

print(format)