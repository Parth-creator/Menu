def search(list, n):
    l = 0
    u = len(list) - 1
    index = int

    while l <= u:
        mid = (l + u) // 2

        if list[mid] == n:
            index = list.index(n)
            print(n, 'is on index:', index)
            break

        else:
            if list[len(list) - 1] == n:
                index = list.index(n)
                print(n, 'is on index:', index)
                break

            if list[mid] < n:
                l = mid
                mid = (l + u) // 2
                pass
            if list[mid] > n:
                u = mid
                mid = (l + u) // 2
                pass

            elif n not in list:
                print("Value not found")
                break

l1 = [1, 2, 3, 4, 5]

search(l1, 6)
