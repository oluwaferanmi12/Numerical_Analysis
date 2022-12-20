def do_forward(x_values , y_values):
    current_difference = y_values
    while(len(current_difference) > 1):
        new_difference = []
        for i in range(len(current_difference) - 1):
            new_entry = round(current_difference[i + 1] - current_difference[i] , 2)
            new_difference.append(new_entry)


        current_difference = new_difference
        print(current_difference)







do_forward([9,10,11,12,13,14] , [5,5.4, 6 , 6.8 , 7.5 , 8.1])