def rectangle(a,b):
    abcd = ""

    abcd += "o" * a 
    abcd += "\n"
    for i in range(a - 2):
        
   
        
        abcd += "o" 
        abcd += " " * a
        abcd += "o" 
        abcd += "\n"
        
    abcd += "o" * (a + 2)
    return abcd

# telo programu
data = input().split()
print(rectangle(int(data[0]), int(data[1])))