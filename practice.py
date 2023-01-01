has_good_credit = True
has_criminal_record = True
if has_good_credit and not has_criminal_record:
    print('Eligible for loan')
else:
    print('Not eligible for loan')
print('Loan eligibility checked\n\n')

temp = 13

if temp > 30:
    print("It's a hot day")
elif temp < 10:
    print("It's a cold day")
else:
    print("It's neither a cold or hot day\n\n")
#program to check lenght of character

name = str(input('Please, Enter your name '))

if len(name) <= 3:
    print('Name must be more than 3 characters')
elif len(name) > 50:
    print('Name must not be more that 50 characters')
else:
    print('Your name is ', name)
    print('Name looks good\n\n')


#A weight converter program

weight = int(input('Enter Weight '))
unit = input('Enter unit ' ' = ' ' (l)bs ' ' (k)g ')
conversion_rate = 0.5
if unit == 'l':
    convert = weight * conversion_rate
    print(f'You are: {convert} pounds')
elif unit == 'g':
    convert = weight / conversion_rate
    print(f'You are: {convert} Kilos')
else:
    print('Invalid Unit')