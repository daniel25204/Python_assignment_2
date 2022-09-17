file = input("Enter the filename : ")
if len(file) < 1:
    file = "mbox-short.txt"
nums = []
with open(file) as f:
    for line in f:
        if line.startswith("X-DSPAM-Confidence"):
            start = line.find('0')
            num = float(line[start : ])
            nums.append(num)
    
sum = 0
for n in nums:
    sum += n
result = sum/len(nums)

print("Average spam confidence: ", result)