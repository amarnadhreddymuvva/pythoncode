with open ("amar.txt","r") as f:
    j=""
    for i in f:
        j=i+j

print(j)