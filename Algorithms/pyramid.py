i = input("Enter the number of rows: \n")

for j in range(int(i) + 1):
    print('x' * j)

for j in range(int(i) + 1):
    print((int(i) - j) * ' ' + 'x' * j)

for j in range(int(i) + 1):
    print((int(i) - j) * ' ' + 'x' * j + 'x' * (j - 1))
