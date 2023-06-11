from collections import deque

def validate_brackets(n):
    """
    Validates the correctness of brackets in a given expression.

    Args:
        n (str): The expression containing brackets to be validated.

    Returns:
        bool: True if all brackets are properly closed, False otherwise.
    """
    open_bracket = ['{', '(', '[']
    close_brackets = ['}', ')', ']']
    stack = deque()
    queue = deque()

    for i in n:
        if i in open_bracket:
            stack.append(i)
            queue.append(i)
        elif i in close_brackets:
            index = close_brackets.index(i)
            if len(stack) > 0 and open_bracket[index] == stack[-1]:
                stack.pop()
            else:
                return False
            if len(queue) > 0 and open_bracket[index] == queue[0]:
                queue.popleft()
            else:
                return False

    if len(stack) == 0 and len(queue) == 0:
        return True
    else:
        return False

# Test the function
expression = input("Enter an expression: ")
result = validate_brackets(expression)
print("Result:", result)
