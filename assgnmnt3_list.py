fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line = line.rstrip()
    word = line.split()
    for x in word:
       if x in lst:
           continue
       else:
           lst.append(x)
     
lst.sort()
print(lst)

