#Simple Calculator

first_number = input('-> ')
operation_sign = input('Operation_sign ->')
second_number = input('-> ')
result =""

if operation_sign == '+':
    result = int(first_number) + int(second_number)
    print(result)
else:
    print("")
if operation_sign == '-':
    result = int(first_number) - int(second_number)
    print(result)
else:
    print("")
if operation_sign == '*':
    result = int(first_number) * int(second_number)
    print(result)
else:
    print("")
if operation_sign == '/':
    result = int(first_number) // int(second_number)
    print(result)
else:
    print("")

