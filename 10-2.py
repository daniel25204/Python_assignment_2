file = input("Enter the filename : ")
if len(file) < 1:
    file = "mbox-short.txt"
hours = []
with open(file) as f:
    for line in f:
        if line.startswith("From "):
            hours.append(int(line.split(' ')[6][:2]))
hours_set = set(hours)
result = []
for h in hours_set:
    if(h < 10):
        str_h= '0' + str(h)
    else:
        str_h= str(h)
    result.append([str_h, hours.count(h)])

for x in result:
    print(x[0], x[1])