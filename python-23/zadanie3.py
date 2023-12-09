capacity = int(input())
user_input = str(input())

# split user input into array
array = user_input.split(",")
input_array = array[::2]
output_array = array[1::2]

length = len(input_array)
    
input_num = 0
output_num = 0
current_capacity = 0
current = 0
was_ever_full = False


i = 0
while i < len(input_array):

    current_capacity = int(input_array[i]) - int(output_array[i])
    current += current_capacity
    
    if current > capacity:
        print(i, current - capacity)
        was_ever_full = True
   
    i += 1


if not was_ever_full:
    print("ani raz")