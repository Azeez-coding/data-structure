lst = ['apple','banana','orange','mango']

print("length of list:",len(lst))
print("first element:",lst[0])
print("last element:",lst[-1])

lst.append('papya')
print("update list:", lst)

lst.remove('banana')
print("update list:", lst)

lst.sort()
print("sorted list:", lst)

lst.pop(1)
print("update list:", lst)

lst.reverse()
print("reversed list:", lst)

print("multiplicationon list:", lst)
 
lst.clear()
print("update list:",lst)