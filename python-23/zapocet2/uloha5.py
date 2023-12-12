# Na vstupe je zadaná veta = slová oddelené medzerami.
# Zabezpečte, aby sa vytvoril nový zoznam, ktorý nebude obsahovať slová obsahujúce "o"/"O" alebo "a"/"A".
# Použite List comprehension - inak max. 50 percent bodov.
# Vstup: Dnes je na Slovensku jesenné počasie.
# Výstup: Dnes je jesenné



# newlist = [expression for item in iterable if condition == True]
user_input = input().split()

newlist = [word for word in user_input if "o" not in word and "O" not in word and "a" not in word and "A" not in word]
    
print(" ".join(newlist))