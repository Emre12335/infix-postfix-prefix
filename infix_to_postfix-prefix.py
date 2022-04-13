operators = {'+': 1, '-': 1, '*': 2, '/': 2}  # operators priority numbers


# if number is higher priority of the operator is higher


def ifpf(str1: str):
    m_str = ""  # result of conversion
    o_stack = []  # stack for operators
    case = 0  # paranthesis number
    for i in str1:  # scanning given string
        if i not in operators and i != "(" and i != ")":
            m_str += i  # adding character to result if it is operand
            continue
        if i == "(":
            case += 1
            o_stack.append(i)
            # if operator is open paranthesis we increase paranthesis number and then add open paranthesis to stack
            continue
        if i == ")" and case:
            while o_stack[-1] != "(":
                m_str += o_stack.pop()
            o_stack.pop()
            case -= 1
            # if operator is close paranthesis we add all operators to result untill we get to open paranthesis
            # after we pop out open parathesis and decrease paranthesis number
        if i in operators:
            if len(o_stack) == 0 or o_stack[-1] == "(" or operators[o_stack[-1]] < operators[i]:
                o_stack.append(i)
                # if the stack is empty or last member is open paranthesis
                # or the stack's last member is smaller than current operand
                # we add current operand to the stack
            elif operators[o_stack[-1]] >= operators[i]:
                while len(o_stack) != 0:
                    if o_stack[-1] == "(":
                        break
                    if operators[o_stack[-1]] < operators[i]:
                        break
                    m_str += o_stack.pop()
                o_stack.append(i)
                #  if the stacks last member is greater than or equal to current operand
                # unless the stack is empty
                # untill we get "(" or
                # stacks last member is smaller than current operand we push the stacks members
    while len(o_stack) != 0:
        m_str += o_stack.pop()
        # at the end we add all operators in the stack to result
    return m_str  # then return string


# infix to prefix can be handled by ifpf with steps below

# 1) reverse the given string paranthesis are reversed get them correct
# 2) apply ifpf function
# 3) reverse the result

def replaces(str1: str):
    nstr = ""
    for i in str1:
        if i != "(" and i != ")":
            nstr += i
        elif i == "(":
            nstr += ")"
        else:
            nstr += "("
    return nstr


def ifpref(str1: str):
    nstr = str1[::-1]  # reverse the string
    nstr = replaces(nstr)  # replace "(" and ")" with their opposites
    nstr = ifpf(nstr)  # applt ifpf
    return nstr[::-1]  # reverse the result and return

print(ifpf("5+3*9"))
#print(ifpf(""))
#print(ifpf(""))
print(ifpref("5+3*9"))
#print(ifpref(""))
#print(ifpref(""))

