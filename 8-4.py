file = input("Enter the filename : ")
if len(file) < 1:
    file = "romeo.txt"
word_list = []
with open(file) as f:
    for line in f:
        splitted_line = line.rstrip().split(' ')
        for word in splitted_line:
            if word not in word_list:
                word_list.append(word)

word_list.sort()
print(word_list)