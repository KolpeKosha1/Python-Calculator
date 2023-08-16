A = int(input("The first value is: "))
B = int(input("The second value is: "))
C = input("The function you want to perform: ")

if C == '+':
    print('The Sum is: ', A + B)
elif C == '-':
    print('The Subtraction is: ', A - B)
elif C == '*':
    print('The Multiplication is: ', A * B)
elif C == '/':
    print('The Division is: ', A / B)
elif C == '%':
    print('The Modulus is:', A % B)
elif C == '//':
    print('The Floor division: ', A // B)
else:
    print("Error")
