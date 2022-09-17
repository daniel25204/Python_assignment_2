file = input("Enter the filename : ")
if len(file) < 1:
    file = "mbox-short.txt"
senders = {}
with open(file) as f:
    for line in f:
        if line.startswith("From "):
            email = line.split(' ')[1]
            if not senders.get(email):
                senders[email] = 1
            else:
                senders[email] += 1

max_sender = []
max_num = 0
for k,v in senders.items():
    if v > max_num:
        max_num = v
        max_sender = [
            k, v
        ]
    
print(max_sender[0], max_sender[1])