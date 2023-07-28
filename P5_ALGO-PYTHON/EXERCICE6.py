b=int(input("donner l'ordre de la matrice: \n"))
menu=input("choisi un menu : \n ")
color=input('choisi une couleure : \n')
M=[]
if b>=5:
    liste=[]
    for i in range(b):
        liste=[]
        for j in range(b):     
            liste.append("    ")
        M.append(liste) 
if menu=='ADDP':

    for i in range(b):
        for j in range(b):
            M[j][i]=menu
            if j<i:
                M[j][i]="   "      
            print(M[j][i],end='    ')
        print("\n")
elif menu=='EDDP':
    for i in range(1,b):
        for j in range(b):
            
            if j<i:
                M[i][j]=menu  
            print(M[i][j],end='    ')

        print("\n")
elif menu=='SDP':
    for i in range(b):
        for j in range(b):
            if i==j:
                M[i][j]=menu
            else:
                M[i][j]='   '
            print(M[i][j],end='    ')
        print("\n")

elif menu=='ADDS':
    for i in range(1,b):
        for j in range(b):
            if j>=i:
                M[i][j]=menu  
                print(M[i][j],end='    ')

        print("\n")
elif menu=='EDDS':
    for i in range(1,b):
        for j in range(b):
            M[i][j]='    '
            if j>=b-i:
                M[i][j]=menu 
                
            print(M[i][j],end='    ')
        print('\n')


elif menu=='SDS':
    for i in range(b):
        for j in range(b):
            if i!=j:
                M[i][i]='    '
                print(M[i][j],end='    ')
            else:
                M[i][j]=menu
            print(M[i][j],end='    ')
        print("\n")
else :
    print('vous n''avez pas choisi le bon menu, prend ton choix sur(ADDP,EDDP,EDP,ADDS,EDDS,EDS) ')

print('---------------------------------------------------')
print('vous avez choisi le menu',menu,'colore en',color)

def matri(menu,color):
    M=[]
    if b>=5:
        liste=[]
        for i in range(b):
            liste=[]
            for j in range(b):     
                liste.append("    ")
            M.append(liste) 
    if menu=='ADDP':
    
        for i in range(b):
            for j in range(b):
                M[j][i]=color
                if j<i:
                    M[j][i]="     "      
                print(M[j][i],end='    ')
            print("\n")
    elif menu=='EDDP':
        for i in range(1,b):
            for j in range(b):
                
                if j<i:
                    M[i][j]=color   
                print(M[i][j],end='    ')

            print("\n")
    elif menu=='SDP':
        for i in range(b):
            for j in range(b):
                if i==j:
                    M[i][j]=color
                else:
                    M[i][j]='    '
                print(M[i][j],end='    ')
            print("\n")

    elif menu=='ADDS':
        for i in range(1,b):
            for j in range(b):
                if j>=i:
                    M[i][j]=color  
                    print(M[i][j],end='    ')

            print("\n")
    elif menu=='EDDS':
        for i in range(1,b):
            for j in range(b):
                M[i][j]='     '
                if j>=b-i:
                    M[i][j]=color  
                    
                print(M[i][j],end='    ')
            print('\n')


    elif menu=='SDS':
        for i in range(b):
            for j in range(b):
                if i!=j:
                    M[i][i]='    '
                    print(M[i][j],end='    ')
                else:
                    M[i][j]=color
                print(M[i][j],end='    ')
            print("\n")
    else :
        print('vous n''avez pas choisi le bon menu, prend ton choix sur(ADDP,EDDP,EDP,ADDS,EDDS,EDS) ')
        
matri(menu,color)