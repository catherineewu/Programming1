op_one = float(input('Enter first operand: '))
op_two = float(input('Enter second operand: '))
print('\nCalculator Menu\n---------------\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n')
op = int(input('Which operation do you want to perform? '))

if 1 <= op <= 4:
    true = 1
    if op == 1:
        result = op_one + op_two
    elif op == 2:
        result = op_one - op_two
    elif op == 3:
        result = op_one * op_two
    elif op == 4:
        result = op_one / op_two
else:
    true = 0

if true == 0:
    print('\nError: Invalid selection! Terminating program.')
if true == 1:
    print('\nThe result of the operation is', result, end='. Goodbye!')