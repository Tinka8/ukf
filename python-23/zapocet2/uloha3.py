path = "file1.txt"

try:
    f = open(path, "r")
except FileNotFoundError:
    print("neexistujúci súbor")