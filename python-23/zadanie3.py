kapacita = 30
user_input = "20,0,20,5,10,10,5,0"

aaa = user_input.split(",")


print(aaa)

vstup = aaa[::2]
vystup = aaa[1::2]

print(f"vstup {vstup}")
print(f"vystup {vystup}")


vstup = map(int, vstup)
vystup = map(int, vystup)


time = 0

for i in vstup:
    time += 1
    if i > kapacita:
        print(f"{time} {i - kapacita}")
        
    
