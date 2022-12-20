def evaluateFunction(x , func):
    return eval(func)

def solve_using_linear_iteration( func , initialValue = None , first_interval = None , second_interval = None ):
    if( not initialValue and not first_interval  and not second_interval ):
        print("Atleast an intial value or two points with which the root can be found is required");
        return
    
    elif((initialValue and first_interval) or (initialValue and second_interval)):
        print("if there is an initial , there is no need for either first interval or second interval! , Retry!!!");
        return

    elif(first_interval and not second_interval or not first_interval and second_interval):
        print("if initial value is not to be used , then there is need for the two values, first_interval and second_interval")
        return
    # Setting the intial value of x
    if(initialValue):
        x_i = float(initialValue) 
    else:
        x_i = float(first_interval)  if  abs(evaluateFunction(float(first_interval), func)) < abs(evaluateFunction(float(second_interval)
        , func)) else float(second_interval) 
    

    for i in range(5):
       currentValue = evaluateFunction(float(x_i), func)
       if(abs(currentValue - x_i) < 0.001):
           print(currentValue)
           break
    
       x_i = currentValue
        

# Note: The function should be expressed in the form of x=g(x)
# The expected parameters are also the function , and an initial value

# solve_using_linear_iteration("(1/3 * (1 + x**2))" , initialValue="0" );
# solve_using_linear_iteration(("1/5 * (1 + x**3)") , initialValue="4" ,first_interval="0" , second_interval="1");


# func = "x + 3"
y = 7
x = 5
print(eval("x + y + 3"))


    