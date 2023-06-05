# function called validate brackets

def validate_brackets(n):

    open_bracket = ['{','(','[']
    close_brackets = ['}',')',']']
    list=[] 

    for i in n:
        
        if i in open_bracket:
            list.append(i) 
        elif i in close_brackets:
            index=close_brackets.index(i) 
            if len(list)>0 and open_bracket[index]==list[len(list)-1]:
                list.pop()
            else:
                return False
            
    if len(list)==0:
        return True
    else:
        return False