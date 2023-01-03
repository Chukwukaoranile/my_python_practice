# A program that calculates the return on investment after 10 years
invest = input('Enter your investment ')
interest_rate = input('Enter interest rate ')
invest = float(invest)
interest_rate = float(interest_rate) * .01 # This '* .01' rounds the float to 2 decimal places
for i in range(1, 11):
    invest = invest + (invest * interest_rate)
    print('Return on Investment after {} year(s) ${:.2f}'.format(i, invest))