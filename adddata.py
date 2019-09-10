context=open("amar.txt","r").readlines()

context_set=set(context)
context1=open("amar1.txt","r").readlines()

context_set1=set(context1)


cleandata=open('clean.txt','w')
for line in set(context) and set(context1):
    cleandata.write(line)