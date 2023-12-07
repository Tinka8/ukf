user_input = str(input())

# initiate variables to store values
summ = 0 
index = 0
pin_number = ""


# get first 2 digits
first_two = user_input[:2]
if '0' in first_two:
    index = 1



# get sum of first 2 digits 
for i in first_two:
    int_ = int(i)
    summ += int_
    
# num of chars removed from string 
index += summ

# get first chars based on sum of first 2 digits
result = user_input[:index]

# store pin num
final_result = result[summ-1]
pin_number += final_result

# create new string using remaining chars 
new_string = user_input[index:] 



while len(new_string) > 0:
    
    # initiate variables to store values
    summ = 0 
    index = 0
    

    # get first 2 digits
    first_two = new_string[:2]
    if '0' in first_two:
        index = 1  

    # get sum of first 2 digits 
    for i in first_two:
        int_ = int(i)
        summ += int_
        
    
    if len(new_string) < summ:
        break

        
    # num of chars removed from string 
    index += summ
    
    if summ > len(new_string):
        break


    # get first chars based on sum of first 2 digits
    result = new_string[:index]
   

    # store pin num
    final_result = result[summ-1]
    pin_number += final_result
    

    # create new string using remaining chars 
    new_string = new_string[index:] 


    if len(new_string) == 0:
        break
    

print(f"{pin_number}")