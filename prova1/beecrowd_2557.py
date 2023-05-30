def solve(equation):

    left,right = equation.split('=')
    op1,op2 = left.split('+')

    if op1 == 'R':
        ans = int(right)-int(op2)
    elif op2 == 'L':
        ans = int(right)-int(op1)
    else:
        ans = int(op1)+int(op2)

    return ans

while True:

    try:
        eq = input()
        print(solve(eq))
    except EOFError:
        break
