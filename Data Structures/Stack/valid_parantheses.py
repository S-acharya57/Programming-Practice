# string s has characters (){}[]
# s is valid iff every open bracket is closed by the same type of close bracket
# open brackets are closed in correct order
# every close bracket has correspondinng open bracket of the same type
# 
from stack_ import StackDS as stack

def isValid(s:str)->bool:
    """
    Function to validate a string that follows the condition

    s(str): String to check for the validation

    Returns bool value of its validity
    """ 
    stack_instance = stack()
    
    open_brackets =["(", "[", "{"]
    close_brackets = [")", "]", "}"]
    
    for el in s:
        # print(f'\t\t{el}')
        stack_instance.displayAll()
        # print(f'Stack is for {el}: {}\n')
        # if(stack_instance.isEmpty()):
        #     stack_instance.push(el)
        if el in open_brackets:
            stack_instance.push(el)

        elif el in close_brackets:
            last = stack_instance.pop()
            if open_brackets.index(last) == close_brackets.index(el):
                continue
            else:
                # print(f'{open_brackets.index(last)} not match with {close_brackets.index(el)}')
                
                f"{last} does not correspond to {el}"
                return False

    # print(f'{stack_instance.displayAll()}')
    if(stack_instance.isEmpty()):
        return True
    # else:
    #     # print("Stack is not empty")
    #     # print(f'{stack_instance.displayAll()}')
    #     pass

inp = input("Enter the string of parantheses")

if isValid(inp):
    print("YESSSSSSS")
else:
    print('NOOOOO')
        