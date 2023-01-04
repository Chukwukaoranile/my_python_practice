# Using Formatters to Organize Data

for i in range(3, 13):
    print(i, i * i, i * i * i)

for i in range(3, 13):
    print("Result = {:3d} {:4d} {:5d}".format(i, i * i, i * i * i))
'''
    We can also manipulate the alignment of the columns by adding <, ^, and > 
    for text alignment, change d to f to add decimal places, change field name
     index numbers, and more to ensure that we are displaying the data as we would like.'''
