path = "file1.txt"

try:
    f = open(path, "r")
except FileNotFoundError:
    print("neexistujúci súbor")
    exit()


for line in f:  
    array = line.split()
  
    if array[1] == "*":
        print(array[0],  "*", array[-1], "=", int(array[0]) * int(array[-1]))
    elif array[1] == "-":
        print(array[0],  "-", array[-1], "=", int(array[0]) - int(array[-1]))    
    elif array[1] == "+":
        print(array[0],  "+", array[-1], "=", int(array[0]) + int(array[-1]))
        
   
f.close()
