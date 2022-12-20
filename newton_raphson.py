def resolveValue(func , a , b):
    value_1 = getValue(func , a)
    value_2 = getValue(func, b)
    # TODO what if we the evaluation of this gives zero , what are we supposed to do in the case ?, it's definitely a root , what then should be done
    if(value_1 * value_2 >= 0):
        return False
    
    return True

def solve_using_newton_raphson(func_1 , func_2 , interval , interval_1 = None):
    # if there is just an interval , then it means we can assume we can start computation with just one 
    print("i got called")
    if(interval and (not interval_1)):
        x_i = interval
    elif(interval and interval_1):
        if( not resolveValue(func_1, interval, interval_1)):
            print("Incorrect interval entered")
            return
        # Now , check the smallest value of either interval or interval_1 
        x_i = interval if abs(getValue( func_1 , interval)) <  abs(getValue(func_1, interval_1)) else interval_1
    
    while True:
        print(x_i)
        currentValue = x_i - (getValue(func_1, x_i)/getValue(func_2, x_i))
        if(abs(currentValue-x_i) < 0.001):
            print(currentValue)
            break
        x_i = currentValue

    
    
def getValue(func, x):
    return eval(func)




solve_using_newton_raphson(("x**3 - 5 * x - 40"), ("(3 * x**2) - 5"), 3 , 4)



