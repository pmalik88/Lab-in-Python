name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name,'r')

mail = list()
for line in handle:    
    if not line.startswith('From:') or not line.startswith('From'):
        continue
    words = line.split()
    mail.append(words[1])

#print(mail)
    
counts = dict()    
for word in mail:
    counts[word] = counts.get(word,0)+1

print(counts)
bigcount = None
bigword = None
for word,counts in counts.items():
   if bigcount is None or counts > bigcount:
        bigword = word
        bigcount = counts
print(bigword, bigcount)     