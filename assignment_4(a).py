def precedence(op):
    if op == '^':
        return 3
    if op in ('*', '/'):
        return 2
    if op in ('+', '-'):
        return 1
    return 0

def to_rpn(expression):
    output = []
    stack = []
    for ch in expression:
        if ch.isalpha():  # operand
            output.append(ch)
        elif ch == '(':
            stack.append(ch)
        elif ch == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            if stack:  # remove '(' safely
                stack.pop()
        else:  # operator
            while (stack and stack[-1] != '(' and
                   ((precedence(stack[-1]) > precedence(ch)) or
                   (precedence(stack[-1]) == precedence(ch) and ch != '^'))):
                output.append(stack.pop())
            stack.append(ch)
    while stack:
        output.append(stack.pop())
    return "".join(output)

# Driver code
if __name__ == "__main__":
    t = int(input("Enter number of test cases: "))
    for _ in range(t):
        expr = input("Enter expression: ").strip()
        print(to_rpn(expr))
