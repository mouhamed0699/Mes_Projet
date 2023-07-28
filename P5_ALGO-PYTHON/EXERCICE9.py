def numero_valide(a):
    if len(a)==9 and (a[0]+a[1]=='78' or a[0]+a[1]=='70' or a[0]+a[1]=='77' or a[0]+a[1]=='76' or a[0]+a[1]=='75' ):
        return a 
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def saisie_operateur():
    reponse=1
    L=[]
    while reponse==1:
        b=input('donner une operateur : ')
        L.append(b)
        reponse=int(input('taper 1 pour continuer ou un autre chiffre pour arreter : '))


    N=len(L)
    M=[]
    for i in range(N):
        F=[]
        F.append(L[i])
        M.append(F)
    return M
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def saisie_info_client():
    T=saisie_operateur()
    N=len(T)
    r=1
    while r==1:   
        prenom=input('donner le prenom du client : ')
        nom=input('donne le nom du client : ')
        numero=input('donne le numero du client : ')
        if numero_valide(numero)==numero:
            for i in range(N):
                M=[]
                if T[i][0]=='Orange' and numero[0]+numero[1] in ['77','78']:
                    M.append(prenom)
                    M.append(nom)
                    M.append(numero)
                    T[i].append(M)
                if T[i][0]=='Expresso' and  numero[0]+numero[1] == '70' :
                    M.append(prenom)
                    M.append(nom)
                    M.append(numero)
                    T[i].append(M)
                if T[i][0]=='Tigo' and  numero[0]+numero[1] == '76':
                    M.append(prenom)
                    M.append(nom)
                    M.append(numero)
                    T[i].append(M)
                elif T[i][0]=='Promobile' and  numero[0]+numero[1] == '75' :
                    M.append(prenom)
                    M.append(nom)
                    M.append(numero)
                    T[i].append(M)
                else:
                    print('invalide')
                M=[]
        r=int(input('Tapez 1 pour continuer la saisie d\'information de client ou autre numero pour arreter : '))
    return T
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
def affichage_matx_clients_operateur(T):
    print('------------------------------------------------------------------------------')
    for i in range(len(T)):
        for j in range(len(T[i])):
            print(T[i][j],end=' ')
        print('\n')
        print('------------------------------------------------------------------------------')
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
def tableau(Liste):
    print('\n')
    for i in range(len(Liste)):
        
        print(' \t {}- {} \t'.format(i+1,Liste[i]))
        print('\n')
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def affichage_client_operatuer(t):
    for i in range(len(t)):
        choix=input('donne un operateur : ')
        if choix in t[i]:
            for j in range(len(t[i])):
                print(t[i][j])

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def affichage_numero_client(T):
    N=len(T)
    b=input('donne le prenom du client : ')
    c=input('donne le nom du client : ')
    for i in range(N):
        for j in range(len(T[i])):
            if b in T[i][j] and c in T[i][j]:
                print(T[i][j])

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def modification(tab):
    tel=input('donne le numero de tel a modifier : ')
    tel1=input('donne le nouveau numero : ')
    if numero_valide(tel)==tel and numero_valide(tel1)==tel1:
        for i in range(len(tab)):
            for j in range(len(tab[i])):
                if tel in tab[i][j]:
                    for k in range(len(tab[i][j])):
                        if tab[i][j][k]==tel:
                            tab[i][j][k]=tel1
    return tab
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def ajouter(T):
    N=len(T)
    prenom=input('donne un prenom : ')
    nom=input('donne un nom : ')
    numero=input('donne un numero :')
    if numero_valide(numero)==numero:
        for i in range(N):
            M=[]
            if T[i][0]=='Orange' and numero[0]+numero[1] in ['77','78']:
                M.append(prenom)
                M.append(nom)
                M.append(numero)
                T[i].append(M)
            if T[i][0]=='Expresso' and  numero[0]+numero[1] == '70' :
                M.append(prenom)
                M.append(nom)
                M.append(numero)
                T[i].append(M)
            if T[i][0]=='Tigo' and  numero[0]+numero[1] == '76':
                M.append(prenom)
                M.append(nom)
                M.append(numero)
                T[i].append(M)
            elif T[i][0]=='Promobile' and  numero[0]+numero[1] == '75' :
                M.append(prenom)
                M.append(nom)
                M.append(numero)
                T[i].append(M)
            else:
                print('invalide')
    return T
                
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def file_text(tab,nom_fichier):
    file=open(nom_fichier,'a')
    for i in range(len(tab)):
        for j in range(1,len(tab[i])):
            for k in range(len(tab[i][j])):
                file.write(str(tab[i][0]))
                file.write(' | ')
                file.write(str(tab[i][j][k]))
                file.write(' ; ')
        file.write('\n')
    file.close()
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------