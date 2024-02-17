# Use the file name mbox-short.txt as the file name
#fname = input("Enter file name: ")
fh = open('new8.txt','r')
sum = 0
count =0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    i =line.find('0')
    data = float(line[i:])
    sum = sum + data
    count = count + 1    
    
print('Average spam confidence: ', sum/count )