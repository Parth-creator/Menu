l1 = [1, 2, 3, 4, 5, 6, 7]

input = input("Enter the key which you want to search: \n")
#print(type(input))

for i in l1:
    if i == int(input):
        print("Your key ", input, " is on the index ", l1.index(i))
if int(input) not in l1:
    print("Sorry key not found\nPls try again")
