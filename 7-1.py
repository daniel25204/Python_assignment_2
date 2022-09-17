file = input("Enter the filename : ")
if len(file) < 1:
    file = "words.txt"
with open(file) as f:
    for line in f:
        print(line.upper().rstrip())