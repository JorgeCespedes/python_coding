
'''Python Program to Check a Number is a Disarium Number'''

number = int(input('Enter the number to check Disarium number: '))
length = len(str(number))
Temp = number
Sum = 0
rem = 0

while Temp > 0:
    rem = Temp % 10
    Sum = Sum + int(rem ** length)
    Temp = Temp // 10
    length = length - 1

print('The Sum of the digits = %d' %Sum)
if Sum == number:
    print('\n%d is a Disarium Number.' %number)
else:
    print('%d is not a Disarium Number.' %number)

