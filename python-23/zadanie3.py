capacity = 10
user_input = "20,0,20,5,10,10,5,0"

# split user input into array
array = user_input.split(",")
input_array = array[::2]
output_array = array[1::2]

length = len(input_array)
print(length)

print(f"input {input_array}")
print(f"output {output_array}")

    
input_num = 0
output_num = 0

i = 0
while i < len(input_array):
    print(i)
    print(f"input {input_array[i]}")
    print(f"output {output_array[i]}")
        
    i += 1
    
    
        
