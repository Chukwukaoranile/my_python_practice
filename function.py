name = "Eric"
age = 74
print("Hello, %s. You are %s." % (name, age))

# 'Hello Eric. You are 74.'
number = 8.8132
print(f"{number} Battery street")
print('Battery street'.format(number))
print('Float: {:0.2f}'.format(number))
str = "Holberton School"
_str = str[0:9]
print('{:s}{:s}{:s}\n{:s}'.format(str, str, str, _str))
str1 = "Holberton"
str2 = "School"
str1 = str1 + " " +str2
print(f"Welcome to {str1}!")
word = "Holberton"

print(f"First 3 letters: {word[:3]}")
print(f"Last 2 letters: {word[7:]}")
print(f"Middle word: {word[1:-1]}")