b=input('Donner une phrase : \n')

C=""

for i in range(1,len(b)):
    if b[i]==b[i-1] and b[i]==" ":
        C=C+""
    else :
        C=C+b[i]

C=b[0]+C
print("la nouvelle phrase enlevant toutes les espaces inutile est  : ",C)  