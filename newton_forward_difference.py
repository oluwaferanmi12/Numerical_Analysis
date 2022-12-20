from math import factorial

def generateDifference(y_values , type):
    current_difference = y_values
    diffVal = []
    if(type == "forward"):
        diffVal.append(y_values[0]);
    else:
        diffVal.append(y_values[-1])
    while(len(current_difference) > 1):
        new_difference = []
        for i in range(len(current_difference) - 1):
            new_entry = current_difference[i + 1] - current_difference[i] 
            new_difference.append(new_entry)


        current_difference = new_difference
        if(type == "forward"):
            diffVal.append(current_difference[0])
        else: 
            diffVal.append(current_difference[-1])
    return diffVal





def obtain_r(step_size , x_values , current_point):

    
    # Assert to use forward or backward difference by checking the point given.
    # Obtain x_o
    use_forward = False
    if(abs(x_values[0] - current_point) < abs(x_values[-1] - current_point)):
        use_forward = True
        x_o = x_values[0]  
    else:
        x_o = x_values[-1]
    
    value_r = (current_point - x_o)/step_size
    return [value_r , use_forward]


def do_factorial(r , n_of_loops):
    r_array = 1
    for i in range(n_of_loops):
        r_array *= r - i
    return r_array

def do_backward_factorial(r , n_of_loops):
    r_array = 1
    for i in range(n_of_loops):
        r_array *= r + i
    return r_array
    

def do_n_forward_difference(r , y_value ):
    # obtain the forward values 
    diffValues = generateDifference(y_value , type = 'forward')
    total_value = []
    for i in range(len(diffValues)):
        if(i == 0):
            total_value.append(diffValues[i])
            continue
        if(i == 1):
            total_value.append(r * diffValues[i])
            continue

        r_resolve = do_factorial(r, i)
        denom_fact = factorial(i)
        c_diffValue = diffValues[i]
        instant_result = (r_resolve * c_diffValue)/denom_fact
        total_value.append(instant_result)

    final_result = sum(total_value)
    return final_result
        
def do_n_backward_difference(r , y_value):
    diffValues = generateDifference(y_value , type = 'backward')
    total_value = []
    for i in range(len(diffValues)):
        if(i == 0):
            total_value.append(diffValues[i])
            continue
        if(i == 1):
            total_value.append(r * diffValues[i])
            continue

        r_resolve = do_backward_factorial(r, i)
        denom_fact = factorial(i)
        c_diffValue = diffValues[i]
        instant_result = (r_resolve * c_diffValue)/denom_fact
        total_value.append(instant_result)

    final_result = sum(total_value)
    return final_result





def n_difference(x_value , y_value , instances):
    # Obtain value of r using the step size 
    for i in range(len(instances)):
        step_size = x_value[1] - x_value[0];
        result = obtain_r(step_size, x_value, instances[i])
        value_r = result[0]
        use_forward = result[1]
        if(use_forward):
            result = do_n_forward_difference(value_r , y_value )
            print("The expected value at" , instances[i] , "is" , result )
        else:
            result = do_n_backward_difference(value_r , y_value)
            print("The expected value at" , instances[i] , "is" , result )



n_difference([1891 , 1901 , 1911 , 1921, 1931] , [46 , 66 , 81 , 93 , 101] , [1895 , 1925])