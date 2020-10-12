def sort(list):
    i = 0
    j = 0
    for i in range(len(list)):
        for j in range(len(list)):
            if list[i] < list [j]:
                temp = list[i]
                list[i] = list[j]
                list[j] = temp


l1 = [1, 5, 2, 9, 3]
print(l1)
sort(l1)
print(l1)