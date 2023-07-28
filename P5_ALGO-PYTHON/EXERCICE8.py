# la function bonne_note retourne une note compris entre 0 et 20
def bonne_note(note):

    if note>=0 and note<=20:
        return note
# numero_valide retourne un numero valide
def numero_valide(a):
    if len(a)==9 and (a[0]+a[1]=='78' or a[0]+a[1]=='70' or a[0]+a[1]=='77' or a[0]+a[1]=='76' or a[0]+a[1]=='75' ):
        return a 

# la fonction saisie_affichage permet de saisir et d'afficher un tableau
def saisie(tab):
    
    reponse=1
    while reponse==1:
        L=[]
        prenom=input('donner votre prenom : ')
        L.append(prenom)
        
        nom=input('donner votre nom : ')
        L.append(nom)
        
        Telephone=input('donner le numero de telephone : ')
        while numero_valide(Telephone)!=Telephone:
            Telephone=input('donner une bonne numero de telephone : ')
        L.append(Telephone)
        
        classe=input('donner votre classe : ')
        L.append(classe)
        
        note_devoir=float(input('donner la note du devoir : '))
        while bonne_note(note_devoir)!=note_devoir:
            note_devoir=float(input('donner une note de devoir compris entre 0 et 20 : '))
        L.append(note_devoir) 
        
        note_proj=float(input("donner la note du projet : "))
        while bonne_note(note_proj)!=note_proj:
            note_proj=float(input('donner une note de projet compris entre 0 et 20  : '))
        L.append(note_proj) 
        
        note_Exam=float(input("donner la note de l\' examen : "))
        while bonne_note(note_Exam)!=note_Exam:
            note_Exam=float(input('donner une note d\' examen compris entre 0 et 20  : '))
        L.append(note_Exam) 
        
        moyenne=round((note_devoir+note_proj+note_Exam)/3,2)
        L.append(moyenne)

        tab.append(L)
        L=[]
        reponse=int(input('ftapez 1 pour continuer a ajouter ou un autre numero pour arreter : \n'))
    return tab
#-----------------------------------------------------------------------------------------------------------------------------------------------

def affichage(tab):
    entete()

    for i in range(len(tab)):
        #print('|\t'+str(tab[i][0]),end='')
        for j in range(7):
            print('|   '+str(tab[i][j])+(15-len(str(tab[i][j])))*' ',end='')
        print('|   '+str(tab[i][7])+(15-len(str(tab[i][7])))*' ' +'|',end='')
        print('\n')
    print((153)*'-')
#-------------------------------------------------------------------------------------------------------------------------------------------------
def trier(L):
    N=len(L)

    for i in range(N):
        for j in range(N):
            while L[i][N-1]>L[j][N-1]:
                L[i],L[j]=L[j],L[i]
    return L 
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
    
def recherche(tab):
    b=input('Selectionne une critere de recherche parmis( Telephone,nom, prenom,classe) : \n')
    
    if b=='Telephone':
        c=input('donner le numero de telephone:\n')
        for i in range(1,len(tab)):
            if tab[i][2]==c:
                for j in range(8):
                    print(tab[i][j],end='     ')
    elif b=='nom':
        n=input('donner le nom :\n')
        for i in range(1,len(tab)):
            if tab[i][1]==n:
                for j in range(8):
                    print(tab[i][j],end='     ')
    elif b=='prenom':
        p=input("donner le prenom :\n")
        for i in range(1,len(tab)):
            if tab[i][0]==p:
                for j in range(8):
                    print(tab[i][j],end='     ')
    elif b=='classe':
        cl=input("donner la classe :\n")
        for i in range(1,len(tab)):
            if tab[i][3]==cl:
                for j in range(8):
                    print(tab[i][j],end='     ')
    else:
        print('vous navez pas selectionner le bon critere')

#-----------------------------------------------------------------------------------------------------------------------------------------
def modification(tab):
    tel=input('donne le numero de tel')
    for i in range(len(tab)):
        if tab[i][2]==tel:
            n1=float(input('modifie la note de devoir : '))
            n2=float(input('modifie la note du projet : '))
            n3=float(input('modifie la note de l examen: '))
            if bonne_note(n1)==n1 and bonne_note(n2)==n2 and bonne_note(n3)==n3:
                tab[i][4]=n1
                tab[i][5]=n2
                tab[i][6]=n3
            else:
                print('vous devez donner des note comprisent entre 0 et 20')
    return tab
#---------------------------------------------------------------------------------------------------------------------------------------
def entete():
    
    print((152)*'-')
    print('|   '+'Prenom'+(15-len('Prenon'))*' '+'|   '+'Nom'+(15-len('Nom'))*' '+'|   '+'Telephone'+(15-len('Telephone'))*' '+'|   '+'Classe'+(15-len('Classe'))*' '+'|   '+'Dev'+(15-len('Dev'))*' '+'|   '+'Proj'+(15-len('Proj'))*' '+'|   '+'Exam'+(15-len('Exam'))*' '+'|   '+'Moyenne'+(15-len('Moyenne'))*' '+'|')
    print((153)*'-')

#---------------------------------------------------------------------------------------------------------------------------------------------
def tableau(Liste):
    print('\n')
    for i in range(len(Liste)):
        
        print(' \t {}- {} \t'.format(i+1,Liste[i]))
        print('\n')
  
#-------------------------------------------------------------------------------------------------------------------------------------------------
def file_text(tab,nom_fichier):
    file=open(nom_fichier,'a')
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            file.write(str(tab[i][j]))
            file.write(' ; ')
        file.write('\n')
    file.close()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#trier(saisie(tab))
#affichage(trier(saisie(tab)))SS
