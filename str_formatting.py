open_string = "Sammy loves {}"
print(open_string.format("open source"))

new_open_string = "Sammy loves {} {}."                      #2 {} placeholders
print(new_open_string.format("open-source", "software"))    #Pass 2 strings into method, separated by a comma

sammy_string = "Sammy loves {} {}, and has {} {}."                      #4 {} placeholders
print(sammy_string.format("open-source", "software", 5, "balloons"))    #Pass 4 strings into method

print("The addition of the {} and {} = {} only".format('a', 'b', 10))
print("Sammy the {} has a pet {}!".format("shark", "pilot fish"))
print("Sammy the {1} has a pet {1}!".format("shark", "pilot fish")) # indexing can be used to choose what will be included inside the curly braces.
print("Sammy is a {3}, {2}, and {0} {1}!".format("happy", "smiling", "blue", "shark"))
print("Sammy is a {3}, {2}, and {1} {0}!".format("happy", "smiling", "blue", "shark"))
print("Sammy the {0} {1} a {pro}.".format("shark", "made", pro="pull request")) # This example shows the use of a keyword argument being used with positional arguments.
print("Sammy ate {0:f} percent of a {1}!".format(75, "pizza"))
print("Sammy ate {0:.3f} percent of a pizza!".format(75.765367))
print("Sammy ate {0:.3f} percent of a pizza!".format(75.765367)) # rounds the float to 3 decimal places
print("Sammy has {0:4} red {1:16}!".format(5, "balloons")) # increasing field size
print("Sammy has {0:<4} red {1:^16}!".format(5, "balloons")) # left align
print("{:*<20s}".format("Sammy")) # replacing the empty spaces above with '*'. The arrow '<' determines where the characters will display
print("Sammy ate {0:<10.2f} percent of a pizza!".format(75.765367))

# using Variable
vab = 800
print("Sammy has {} balloons today!".format(vab))

# Ex 2
sammy = "Sammy has {} balloons today!"
var = 800
print(sammy.format(var))