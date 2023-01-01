matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matrix[2][2] = 100 #changes the value from 9 to 100
print(matrix[0]) #prints [1, 2, 3]
print(matrix[0][1]) #prints 2
print(matrix[2][2]) #prints 100 because the item was modified

#Nested loops to print all the numbers in the matrix
for row in matrix:
    for num in row:
        print(num)