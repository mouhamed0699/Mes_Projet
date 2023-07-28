b=int(input("donner l' ordre d'une matrice superieure ou egale à 5 : \n "))
choix=input('choisir une couleur : \n')

print("-------------------")
M=[]
if b>=5:
    liste=[]
    for i in range(b):
        liste=[]
        for j in range(b):     
            liste.append("     ")
        M.append(liste) 
else:
    print('vous devez donner une orde superieur ou egal a 5')
if choix=='bleue':
    
    for i in range(b):
        for j in range(b):
            M[j][i]= "\033[0;34m B \033[0m"
            if j<i:
                M[j][i]="   "      
            print(M[j][i],end='    ')
        print("\n")
elif choix=='rouge':
    for i in range(1,b):
        for j in range(b):
            if j<i:
                M[i][j]="\033[0;31m R \033[0m"  
            print(M[i][j],end='   ')

        print("\n")
else:
    print('vous devez donner comme couleurs beue ou rouge')
    
