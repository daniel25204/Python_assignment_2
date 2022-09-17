file = input("Enter the filename : ")
if len(file) < 1:
    file = "mbox-short.txt"
count = 0
with open(file) as f:
    for line in f:
        if line.startswith("From "):
            print(line.split(' ')[1])
            count += 1

print(f'There were {count} lines in the file with From as the first word')