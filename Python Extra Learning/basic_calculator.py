try:
    num1 = int(input('Enter first number : '))
    num2 = int(input('Enter second number : '))
    op = input('Enter your operator : ')

    if op == '+':
        print("The addition is ",num1+num2)
    elif op == '-':
        print("The subtraction is ",num1+num2)
    elif op == '/':
        print("The division is ",num1/num2)
    elif op == '*':
        print("The multiplication is ",num1*num2)
    elif op == '%':
        print("The remainder is ",num1%num2)
    else:
        print('Please enter valid operator')
except ValueError:
    print('Value not a integer input')
except TypeError:
    print('Type error wrong')
except :
    print('anything wrong')
else:
    print('nothing went wrong')
finally:
    print("this is run anyhow")