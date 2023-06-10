# function called validate brackets

# def validate_brackets(n):

#     open_bracket = ['{','(','[']
#     close_brackets = ['}',')',']']
#     list=[] 

#     for i in n:
        
#         if i in open_bracket:
#             list.append(i) 
#         elif i in close_brackets:
#             index=close_brackets.index(i) 
#             if len(list)>0 and open_bracket[index]==list[len(list)-1]:
#                 list.pop()
#             else:
#                 return False
            
#     if len(list)==0:
#         return True
#     else:
#         return False

def validate_brackets(str):
    """
    Validates if the brackets in a given string are balanced.

    Parameters:
    str: The input string to be checked for balanced brackets.

    Returns:
    bool: True if the brackets are balanced, False otherwise.
    """

    stack = []
    brackets = {
        '(': ')',
        '[': ']',
        '{': '}'
    }

    for bracket in str:
        if bracket in brackets.keys():  # Opening bracket
            stack.append(bracket)
        elif bracket in brackets.values():  # Closing bracket
            if not stack or bracket != brackets[stack.pop()]:
                return False

    return len(stack) == 0