# Solving using the bisection method 


def check_interval(a , b , func):
    first_interval = getValue(func, a);
    second_interval = getValue(func, b);
    # The Function is to check if the Two values have opposit values when func is called on it
    if(first_interval < 0 and second_interval > 0):
        return True
    elif(first_interval > 0 and second_interval < 0):
        return True
    
    return False;


def getValue(func , x):
    return eval(func)


def solve_using_bisection(func , interval_1 , interval_2):
    # Definition of parameter 
    # func = defined function from the question 
    # interval_1 = The first interval for the question
    # interval_2 = The Second interval for the question 
    # error_allowed = The amount of precision that is needed 

    if(not (check_interval(interval_1, interval_2, func))):
        print("The interval is wrong")
        return;
    # Now set the value for positive and negative 
    positive_number = interval_1 if getValue(func, interval_1) > 0 else interval_2
    negative_number = interval_2 if getValue(func, interval_2) < 0 else interval_1

    while True:
        midValue = (positive_number + negative_number )/2
        positive_number = midValue if getValue(func, midValue) > 0 else positive_number
        negative_number = midValue if getValue(func, midValue) < 0 else negative_number
        if(positive_number - negative_number < 0.001):
            print("The root of the function" , positive_number)
            break
        


solve_using_bisection("(5*x**2 + 11 * x - 17)" , 1 , 2 );
# solve_using_bisection(("x**3 + 3*x - 5"), 1, 2)
