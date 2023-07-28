b=input('Donner une chaine de N phrase\n')
C=""
txt=""
for i in range(1,len(b)):
    if (ord(b[i]) in range(48,58)) or (ord(b[i]) in range(65,91)) or (ord(b[i]) in range(97,123)) or (ord(b[i]) in [32,39,33,63,46]):
        if b[i]==b[i-1] and b[i]==" ":
            C=C+""
        else :
            C=C+b[i]
C=b[0]+C
txt=C
s=""
N_de_caractere=[]
chiffre=[]
for i in range(1,len(txt)):
    if (txt[i-1]=='?' and ord(txt[i]) in range(97,123))  or (txt[i-1]=='!' and ord(txt[i]) in range(97,123)) or (txt[i-1]=='.' and ord(txt[i]) in range(97,123)):
        chiffre.append(i)
        s=s+ " " +str(i)       
print("--------------------------------------------------------------------------------------------------------")
print("la nouvelle texte est :  \n", txt)

print("une phrase commence par une lettre majuscule etb se termine par un point ans les indices suivantes",s)
print("--------------------------------------------------------------------------------------------------------")

for i in range(len(chiffre)):
    if i==0:
        N_de_caractere.append(chiffre[i])
        if N_de_caractere[i-1]<25:
            print("la phrase",i+1," doit contenir au moins 25 caracteres")
    else :
        
        N_de_caractere.append(chiffre[i]-chiffre[i-1])
        if N_de_caractere[i-1]<25:
            print("la phrase",i+1," doit contenir au moins 25 caracteres")