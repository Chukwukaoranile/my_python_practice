staff = {
    "name": "Ike Ume",
    "Address": "No. 10 Robinson street, Enugu",
    "Phone No": "+23465789086"
}
# to access the items in the dictionary
staff["Birthdate"] = "17th October, 2001"
print(staff["Birthdate"])
print(staff.get("Name"))# Name, not how it was written in the dictopnary. Allows the program to run and return 'none' intead of showing error message

#program that print phone number  in words
phone = input('Enter Phone No: ')
num_in_word = {
    "+": "plus",
    "0": "zero",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine"
}
output = " "
for fig_num in phone:
    output += num_in_word.get(fig_num, "!") + " "
print(output)