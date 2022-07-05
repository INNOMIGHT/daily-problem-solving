def infix_to_postfix(exp):

    # a*(c+d) -> acd+*

    operands = ('-', '+', '*', '/', '^')
    priority = {'(':0, ')': 0, '+': 1, '-':1, '*': 2, '/':2, "^": 3}
    output = []
    stack = []
    
    for char in exp:
        if char =="(":
            stack.append(char)
        elif char == ")":
            print(stack)
            while stack[-1] != "(":
                output.append(stack.pop())
            stack.pop()
        elif char in operands:
            if stack != []:
                while (priority[stack[-1]] >= priority[char]):
                    output.append(stack.pop())
                    if stack == []:
                        break
            stack.append(char)     
        else:
            output.append(char)

    while stack != []:
        output.append(stack.pop())
    result = ''.join(output)
    return result


print(infix_to_postfix("x^y/(5*z)+2"))

    


