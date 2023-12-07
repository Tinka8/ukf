user_input = "4361871128178134931129"
print(f"user_input {user_input}")


while len(new_string) > 0:
    
    # initiate variables to store values
    summ = 0 
    pin_number = ""


    # get first 2 digits
    first_two = user_input[:2]


    # get sum of first 2 digits 
    for i in first_two:
        int_ = int(i)
        summ += int_
        
    # num of chars removed from string 
    index = summ

    # get first chars based on sum of first 2 digits
    result = user_input[0 : index]


    # store pin num
    final_result = result[-1]
    pin_number += final_result

    # create new string using remaining chars 
    new_string = user_input[7:] 


    if len(new_string) == 0:
        break
    # prints
    print(f"index {index}")
    print(f"result {result} ")
    print(f"sum {summ}")
    print(f"final PIN num {final_result}")
    print(f"new string {new_string}")
