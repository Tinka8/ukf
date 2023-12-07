user_input = str(input())
print(f"user_input {user_input}")

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

print(f"first string {new_string}")
print(f"first pin num {pin_number}")





while len(new_string) > 0:
    
    # initiate variables to store values
    summ = 0 
    


    # get first 2 digits
    first_two = new_string[:2]


    # get sum of first 2 digits 
    for i in first_two:
        int_ = int(i)
        summ += int_
        
    # num of chars removed from string 
    index = summ
    
    if summ > len(new_string):
        break

    # get first chars based on sum of first 2 digits
    result = new_string[0 : index]


    # store pin num
    final_result = result[-1]
    pin_number += final_result

    # create new string using remaining chars 
    new_string = new_string[index:] 
    print(f"create new string using remaining chars  {new_string}")


    if len(new_string) == 0:
        break

    
    
    # prints
    
    print(f"PIN num {final_result}")
    print(f"new string {new_string}")

print(f"FINAL PIN num {pin_number}")