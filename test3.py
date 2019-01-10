def sort_array(source_array):
    l = []
    n = []
    for i in range(len(source_array)):
        if  source_array[i] % 2 != 0:
            l.append(source_array[i])
            n.append(i)
    print(l)
    print(n)


print(sort_array([1,5,6,7,9,1,74,3,2,5]))


