def balanced_parenthesis(str_bal):
    stack = []
    balanced_map = {')':'(', ']': '[','}':'{'}

    for i in str_bal:
        if i in balanced_map.values(): # opening braces
            stack.append(i)
        elif i in balanced_map.keys(): # closing braces
            # verifying if stack is empty if the input is only closing brackets ]]
            
            if not stack or stack.pop() != balanced_map.get(i):
                return False

    return not stack # True if stack is empty

TC, OC: O(n)





print(balanced_parenthesis('(]'))
