capacity = 30
user_input = "35,0,10,20,10,20"

# split user input into array
array = user_input.split(",")
input_array = array[::2]
output_array = array[1::2]

length = len(input_array)

print(f"input {input_array}")
print(f"output {output_array}")

    
input_num = 0
output_num = 0
current_capacity = 0
current = 0


i = 0
while i < len(input_array):

    current_capacity = int(input_array[i]) - int(output_array[i])
    current += current_capacity
    
    if current > capacity:
        print("vysledok -----")
        print(i, current - capacity)
   

    i += 1
    
    if i == len(input_array) and current < capacity:
        print("ani raz")
        break
    
    

