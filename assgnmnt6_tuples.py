name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name,'r')

mail = list()
for line in handle:    
    if line.startswith('From:') or not line.startswith('From'):
        continue
    words = line.split()
    data = words[5]
    i = data.find(':')
    data = data[:i]
    mail.append(data)

#print(mail)
    
counts = dict()    
for word in mail:
    counts[word] = counts.get(word,0)+1

for k,v in sorted(counts.items()):
    print(k,v)