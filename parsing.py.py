#Sohan Pujar 30567556
from math import pow

def tokenization(expr):
    lst = []
    formation = ""
    number = ["1","2","3","4","5","6","7","8","9","0","."]
    x = list(expr) #splitting every list into individual tokens
    for i in range(len(x)):
        if x[i] == " ": #Accounts for whitespace
            continue
        if x[i] in number:
            for j in range(len(number)):
                if x[i] == number[j]:
                    formation += number[j] #concatonate if there is number or dot
        else:
            lst.append(formation) #append the formation of the number
            lst.append(x[i]) #append the tokens
            formation = "" #reset the formation back to empty string
    lst.append(formation) #sometimes can append empty string this accounts if the last index is a number
    while "" in lst:
        lst.remove("") # removes empty strings
    for z in range(len(lst)):
        if lst[z][0] in number:
            lst[z] = float(lst[z])#changes it to float
    return lst

#print(tokenization("(   92   +3)*5-4"))

def has_precedence(op1, op2):
    upper = ["*", "/"] 
    lower = ["+","-"]
    if op1 == "^" and op2 != "^":
        return True #return true if op1 == ^
    elif op1 in upper and op2 in lower:
        return True
    else:
        return False

def simple_evaluation(tokens):
    lst = tokens[:] #got the whole list
    while len(lst) > 1: #while we don't have just a number to finish
        for i in range(0,len(lst),2): #We take steps of 2 to go across all numbers
            if i + 3 < len(lst) - 1: #last operator is len(lst) - 1 
                if has_precedence(lst[i+1], lst[i+3]):
                    x = evaluate(lst[i+1],lst[i], lst[i+2]) #operator, number, number
                    lst[i] = x #put the evaluated bit at that index
                    lst.pop(i+1)#we pop the operator
                    lst.pop(i+1)#we pop the other number
                elif "*" not in lst and "/" not in lst and "+" not in lst and "-" not in lst or "^" not in lst and "+" not in lst and "-" not in lst or "^" not in lst and "*" not in lst and "/" not in lst:
                    x = evaluate(lst[i+1],lst[i], lst[i+2]) #in case it comes up as false
                    lst[i] = #put the evaluated part in that index
                    lst.pop(i+1)#we pop it twice 
                    lst.pop(i+1)
                elif has_precedence(lst[i+3],lst[i+1]) and i+4 == len(lst)-1:
                    x = evaluate(lst[i+3],lst[i+2], lst[i+4])
                    lst[i+2] = x
                    lst.pop(i+3)
                    lst.pop(i+3)
            elif len(lst) == 3: #If we have 3 only tokens
                    x = evaluate(lst[1],lst[0], lst[2])
                    lst[0] = x
                    lst.pop(1)
                    lst.pop(1)
    return lst[0]

def evaluate(op, num1, num2): #evaluating everything
    if op == "^":
        return pow(num1,num2)
    elif op == "+":
        return num1 + num2
    elif op == "*":
        return num1*num2
    elif op == "-":
        return num1 - num2
    elif op == "/":
        return num1/num2

            
#print(simple_evaluation([2, "+", 3, "*", 4, "^", 2, "+", 1]))

def complex_evaluation(tokens):
    lst = tokens
    while "(" in lst and ")" in lst: 
        end = lst.index(")") #grab that index of the end bracket
        for i in range(end, -1, -1): #go back until we reach the open bracket
            if lst[i] == "(":
                start = i #get index of open bracket
                break 
        lst[start:end + 1] = [simple_evaluation(lst[start + 1: end])] #evaluate in between the start and end
    return simple_evaluation(lst)

#print(complex_evaluation(["(", "(", 2, "-", 7, ")", "*", 4,")", "^", 2]))

def evaluation(string):
    return complex_evaluation(tokenization(string))# tokenize the string and evaluate it

#print(evaluation("(2+3)/(5*5)"))

        
