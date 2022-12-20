def do_linear_interpolation (point_1 , point_2 , point=None):
    # Given two points 
    y_0 = point_1[-1]
    y_1 = point_2[-1]
    x_0 = point_1[0]
    x_1 = point_2[0]
    denom_value = x_1 - x_0

    
    left_equation = getEquation(x=x_1, y= y_0 ,denominator= denom_value)
    right_equation = getEquation(x=x_0, y=y_1, denominator = denom_value, second_point=True )
    if(not point):
        print("The Polynomial of the equation is",left_equation ,"-" , right_equation)
    else:
        print("The Polynomial of the equation is",left_equation ,"-" , right_equation)
        print(solveEquation(x_0, x_1, y_0, y_1, a=point))
    


    # according to the formula for interpolation , we obtain the polynomial for the two points
    

def getEquation(x , y , denominator , second_point = False ):
    value_1 = y * x
    value_2 = str(y) + "x"
    if(second_point):
        numerator_1 = "(" + str(value_2) + "-" + str(value_1) + ")" + "/" + str(denominator)
    else:
        numerator_1 = "(" + str(value_1) + "-" + str(value_2) + ")" + "/" + str(denominator)
    return numerator_1;
    
    

def solveEquation(x_0 , x_1 , y_0 , y_1 , a ):
    denominator= (x_1 - x_0)
    right_equation = ((x_1 - a) * y_0)/denominator
    left_equation = ((a - x_0) * y_1)/denominator
    return right_equation + left_equation



do_linear_interpolation( point_1 = [0.82,2.270500] , point_2 = [0.83,2.293319] , point=0.826)