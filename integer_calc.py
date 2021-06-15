# Write a Python program that calculates the sum of three given integers. 
# However, if two of the integers are equal the return value will be zero
num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))
num3 = int(input('Enter the third number: '))
numSum = num1 + num2 + num3

sameNumber = int(0)



if num1 == num1:
    print('The answer is ' + str(sameNumber) + ' because you entered same number')
elif num1 == num2:
    print('The answer is ' + str(sameNumber) + ' because you entered same number')
elif num1 == num3:
    print('The answer is ' + str(sameNumber) + ' because you entered same number')
elif num2 == num1:
    print('The answer is ' + str(sameNumber) + ' because you entered same number')
elif num2 == num2:
    print('The answer is ' + str(sameNumber) + ' because you entered same number')
elif num2 == num3:
    print('The answer is ' + str(sameNumber) + ' because you entered same number')
elif num3 == num1:
    print('The answer is ' + str(sameNumber) + ' because you entered same number')
elif num3 == num2:
    print('The answer is ' + str(sameNumber) + ' because you entered same number')
elif num3 == num3:
    print('The answer is ' + str(sameNumber) + ' because you entered same number')


