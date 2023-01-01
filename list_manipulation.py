list = [20, 34, 17, 20, 34, 100, 56, 90]
list.append(57) # This will add 57 to the list
list_1 = list.copy() # if you print list_1, 100 will appear in the list because it was removed after the copy
list.remove(list[5]) # This method will remove 100 from the list. list.remove(100) will serve same purpose
list.sort() # This will sort the list in ascending order
list.reverse()
print(list)
print(list[5:]) #This will print all the numbers from index 5 to the end