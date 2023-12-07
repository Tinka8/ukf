user_input = str(input())
print(f"user_input {user_input}")

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

print(f"result prvy {result}")

# store pin num
final_result = result[summ-1]
pin_number += final_result

# create new string using remaining chars 
new_string = user_input[index:] 

print(f"first string {new_string}")
print(f"first pin num {pin_number}")

print("---------------")



while len(new_string) > 0:
    
    # initiate variables to store values
    summ = 0 
    index = 0
    

    # get first 2 digits
    first_two = new_string[:2]
    print(f"first two {first_two}")
    if '0' in first_two:
        index = 1
    

    print(f"chytena nula?? {index}")
    

    # get sum of first 2 digits 
    for i in first_two:
        int_ = int(i)
        summ += int_
        
    
    if len(new_string) < summ:
        break

        
    # num of chars removed from string 
    index += summ
    print("=====")
    print(index)
    print(summ)
    print("=====")
  
    
    if summ > len(new_string):
        break


    # get first chars based on sum of first 2 digits
    print(f"index pred novym stringom {index}")
    result = new_string[:index]
   

    #####

  

    # store pin num
    print(f"result ======= {result}")

    
    final_result = result[summ-1]
    print(f"final result {final_result}")
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