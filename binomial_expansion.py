from math import factorial

def resolveValues(value_1 , value_2 , coef):
    
    non_numeric = value_1 if not value_1.isnumeric() else value_2
    numeric = value_1 if value_1.isnumeric() else value_2

    numeric ="+" +" " + str(numeric * coef) if numeric * coef > 0 else str(numeric * coef)
    newVal = numeric + non_numeric
    return newVal

    # The coefficient is always going to be a number 
    # So, all we need to do is ensure we multiply with any of the value that is a number 
    # num_1_value = ""
    # num_2_val = ""
    # if(value_1.isnumeric()):
    #     numeric_val = value_1 *  coef  
    #     num_1_value = numeric_val
    #     return f"{numeric_val} ** {value_2}"
    

    # else:
    #     numeric_val = value_2 * coef
    #     num_2_val = numeric_val
    #     return f"{numeric_val}"

    


def do_binommial(func , power):
    # step 1: Take the function 
    # step 2: Get the operator  
    # check if we have two variable i.e x and y or just one variable and a value i.e x and 1

    newArray = func.split();
    if("+" in newArray):
        operator = "+"
    if("-" in newArray):
        operator = "-"

    variable_1 = newArray[0]
    variable_2 = newArray[2]

    list_of_values = [newArray[0] , newArray[2]]
    # step 3 
    # for c in newArray:
    #     print(c.isnumeric())
    # Now do the expansion 
    answer = ""
    for i in range(power+1):
        coef = factorial(power)/(factorial(power-i) * factorial(i))
        value_1 = int(variable_1)**power-i if variable_1.isnumeric() else f"{variable_1}**{power-i}"
        value_2 = (int(("+" + variable_2 )if operator == "+" else ("-"  + variable_2) ))**i if variable_2.isnumeric() else f"{variable_2}**{i}"
        answer +=" " + resolveValues(value_1 , value_2 , coef)

    return answer
        # Try to multiply the coeeficients, and the respoective values gotten


    
        



result = do_binommial(("x - 3") , 2)
print(result)