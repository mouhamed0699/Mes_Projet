def numero_valide(a):
    Maj=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    chiffre=["0","1","2","3","4","5","6","7","8","9"]
    s=''
    if len(a)==7:
        for i in range(len(a)):        
            if a[i] in chiffre or a[i] in Maj:
                s=s+a[i]  
        if s==a:
            return a
#=======================================================================================================================================================================================
def prenom_valide(a):
    lettre=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P',
            'Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h',
            'i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    s=0
    if a[0] in lettre:
        for i in range(len(a)):
            if a[i] in lettre:
                s=s+1
        if s>=3:
            return a
#=======================================================================================================================================================================================
def nom_valide(a):
    lettre=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    s=0
    if a[0] in lettre:
        for i in range(len(a)):
            if a[i] in lettre:
                s=s+1
        if s>=2:
            return a
#=======================================================================================================================================================================================

def format_date(date):
    d=''
    c=[]
    for i in date:
        if i not in ["0","1","2","3","4","5","6","7","8","9"]:
            d=d+'-'
        else:
            d=d+i
    c=d.split('-')
    for i in range(len(c)):
        if len(c[-1])==2:
            if c[-1]>='24':
                c[-1]='19'+c[-1]
            else:
                c[-1]='20'+c[-1]
    d='-'.join(c)
    return d
def date_valide(date):
    import datetime
    date=format_date(date)
    date_format='%d-%m-%Y'
    try :
        date_valide=datetime.datetime.strptime(date,date_format)
    except ValueError:
        #print('date invalide',date)
        return ' '
    return date
#=======================================================================================================================================================================================

def class_valide(classe):
    if classe[0] in ["3","5","6","4"] and classe[len(classe)-1] in ["A","B"]:
        return classe   
#=======================================================================================================================================================================================


def note_val(note):
    L=[]
    t=[]
    d=[]
    k=[]
    new_note=[]
    L=note.split("#")
    if len(L)==6:
        for c in L:
            t=c.split("[")
            if t[0]=='Anglais' or t[0]=='ANGLAIS':
                if ':' in t[-1]:
                    d=t[-1].split(':')
                    n=''
                    for i in d[-1]:
                        if d[-1]!='':
                            if i!=']':
                                if i==',':
                                    n=n+'.'
                                else:
                                    n=n+i                                     
                    if "0"<n<="20":
                        if '|' in d[0]:
                            k=d[0].split('|')
                            s=''
                            for j in k:
                                for i in range(len(j)):
                                    if j[i]==',':
                                        s=s+'.'
                                    else:
                                        s=s+j[i]
                                if "0"<=s<="20":
                                    new_note.append("True")
            if t[0]=='Francais' or t[0]=='FRANCAIS':
                if ':' in t[-1]:
                    d=t[-1].split(':')
                    n=''
                    for i in d[-1]:
                        if d[-1]!='':
                            if i!=']':
                                if i==',':
                                    n=n+'.'
                                else:
                                    n=n+i                                     
                    if "0"<n<="20":
                        if '|' in d[0]:
                            k=d[0].split('|')
                            s=''
                            for j in k:
                                for i in range(len(j)):
                                    if j[i]==',':
                                        s=s+'.'
                                    else:
                                        s=s+j[i]
                                if "0"<=s<="20":
                                    new_note.append("True")
            if t[0]=='PC' or t[0]=='Pc':
                if ':' in t[-1]:
                    d=t[-1].split(':')
                    n=''
                    for i in d[-1]:
                        if d[-1]!='':
                            if i!=']':
                                if i==',':
                                    n=n+'.'
                                else:
                                    n=n+i                                     
                    if "0"<n<="20":
                        if '|' in d[0]:
                            k=d[0].split('|')
                            s=''
                            for j in k:
                                for i in range(len(j)):
                                    if j[i]==',':
                                        s=s+'.'
                                    else:
                                        s=s+j[i]
                                if "0"<=s<="20":
                                    new_note.append("True")
            if t[0]=='Math' or t[0]=='MATH':
                if ':' in t[-1]:
                    d=t[-1].split(':')
                    n=''
                    for i in d[-1]:
                        if d[-1]!='':
                            if i!=']':
                                if i==',':
                                    n=n+'.'
                                else:
                                    n=n+i                                     
                    if "0"<n<="20":
                        if '|' in d[0]:
                            k=d[0].split('|')
                            s=''
                            for j in k:
                                for i in range(len(j)):
                                    if j[i]==',':
                                        s=s+'.'
                                    else:
                                        s=s+j[i]
                                if "0"<=s<="20":
                                    new_note.append("True")
            if t[0]=='SVT':
                if ':' in t[-1]:
                    d=t[-1].split(':')
                    n=''
                    for i in d[-1]:
                        if d[-1]!='':
                            if i!=']':
                                if i==',':
                                    n=n+'.'
                                else:
                                    n=n+i                                     
                    if "0"<n<="20":
                        if '|' in d[0]:
                            k=d[0].split('|')
                            s=''
                            for j in k:
                                for i in range(len(j)):
                                    if j[i]==',':
                                        s=s+'.'
                                    else:
                                        s=s+j[i]
                                if "0"<=s<="20":
                                    new_note.append("True")
            if t[0]=='HG':
                if ':' in t[-1]:
                    d=t[-1].split(':')
                    n=''
                    for i in d[-1]:
                        if d[-1]!='':
                            if i!=']':
                                if i==',':
                                    n=n+'.'
                                else:
                                    n=n+i                                     
                    if "0"<n<="20":
                        if '|' in d[0]:
                            k=d[0].split('|')
                            s=''
                            for j in k:
                                for i in range(len(j)):
                                    if j[i]==',':
                                        s=s+'.'
                                    else:
                                        s=s+j[i]
                                if "0"<=s<="20":
                                    new_note.append("True")
    if new_note==len(new_note)*['True']:
        return note

#=======================================================================================================================================================================================

def forme_prenom(a):
    d=''
    for i in a:
        if i==' ':
            d=d+''
        else:
            d=d+i
    return d
def forme_nom(a):
    d=''
    for i in a:
        if i==' ':
            d=d+''
        else:
            d=d+i
    return d
def forme_classe(a):
    d=''
    for i in a:
        if i==' ':
            d=d+''
        else:
            d=d+i
    return d
#=======================================================================================================================================================================================

def entete():
    
    print((105)*'-')
    print('|\t'+"\033[91m"+'Numero'+"\033[0m"+(16-len('Numero'))*' '+'|   '+"\033[91m"+'Nom'+"\033[0m"+(16-len('Nom'))*' '+'|   '+"\033[91m"+'Prenom'+"\033[0m"+(16-len('Prenom'))*' '+'|   '+"\033[91m"+'Date de Naissance'+"\033[0m"+(16-len('Date de Naissance'))*' '+'|   '+"\033[91m"+'Classe'+"\033[0m"+(16-len('Classe'))*' '+'|   ')
    print((105)*'-')
#=======================================================================================================================================================================================


def tableau_val_inval(fichier):
    count_line=0
    tableau_valide=[]
    tableau_invalide=[]
    with open(fichier,'r') as f:
        for line in f:
            if count_line>=1:
                x=line.split(',')
                if numero_valide(x[1])==x[1] and nom_valide(x[2])==x[2] and prenom_valide(x[3])==x[3] and date_valide(x[4])==format_date(x[4])  and class_valide(x[5])==x[5] and note_val(x[6])==x[6]: 
                    tableau_valide.append(x[1::])
                else:
                    tableau_invalide.append(x[1::])
                    
            count_line+=1
    return tableau_valide,tableau_invalide
#=======================================================================================================================================================================================


def affichage_valide(fichier):
    entete()
    tableau_valide,tableau_invalide=tableau_val_inval(fichier)
    
    for i in range(len(tableau_valide)):
        tableau_valide[i][1]=forme_nom(tableau_valide[i][1])
        tableau_valide[i][2]=forme_prenom(tableau_valide[i][2])
        tableau_valide[i][3]=format_date(tableau_valide[i][3])
        tableau_valide[i][4]=forme_classe(tableau_valide[i][4])
        tableau_valide[i][5]=(tableau_valide[i][5].replace("#",' '))

    for i in range(len(tableau_valide)):
        print('|\t',end='')
        #for j in range(len(tableau_valide[i])-2):
        print(tableau_valide[i][0]+ (16-len(tableau_valide[i][0]))*' ',end='|   ')
        print(tableau_valide[i][1]+ (16-len(tableau_valide[i][1]))*' ',end='|   ')
        print(tableau_valide[i][2]+ (16-len(tableau_valide[i][2]))*' ',end='|   ')
        print(tableau_valide[i][3]+ (16-len(tableau_valide[i][3]))*' ',end='|   ')

        print(tableau_valide[i][4]+ (16-len(tableau_valide[i][4]))*' ' +'|  ')
        print('\n')
    print(105*'-')
#=======================================================================================================================================================================================

def affichage_invalide(fichier):
    entete()
    tableau_valide,tableau_invalide=tableau_val_inval(fichier)
    for i in range(len(tableau_invalide)):
        for j in range(len(tableau_invalide[i])-1):
            print(tableau_invalide[i][j]+ (16-len(tableau_invalide[i][j]))*' ',end='|   ')
        print(tableau_invalide[i][5]+ (4)*' ',end=' ')
        print('\n')
    print(193*'-')
#=======================================================================================================================================================================================


def recherche_by_num(fichier):
    numero=input('donner un numero :\n')
    tableau_valide,tableau_invalide=tableau_val_inval(fichier) 
    for i in range(len(tableau_valide)):
        if tableau_valide[i][0]==numero:
            print(tableau_valide[i])
       # elif tableau_invalide[i][0]==numero:
            #for j in range(len(tableau_invalide[i])):
                #print(tableau_invalide[i][j]+ (13-len(tableau_invalide[i][j]))*' ',end='|   ')
        #else:
            #return ' '

#=======================================================================================================================================================================================


def head5_valide(fichier):
    entete()
    tableau_valide,tableau_invalide=tableau_val_inval(fichier) 

    for i in range(len(tableau_valide)):
        tableau_valide[i][1]=forme_nom(tableau_valide[i][1])
        tableau_valide[i][2]=forme_prenom(tableau_valide[i][2])
        tableau_valide[i][3]=format_date(tableau_valide[i][3])
        tableau_valide[i][4]=forme_classe(tableau_valide[i][4])
        #tableau_valide[i][5]=(tableau_valide[i][6].replace("#",' '))
    head=0
    for i in range(len(tableau_valide)):
        if head<5:
            print('|\t',end='')
            #for j in range(len(tableau_valide[i])-2):
            print(tableau_valide[i][0]+ (16-len(tableau_valide[i][0]))*' ',end='|   ')
            print(tableau_valide[i][1]+ (16-len(tableau_valide[i][1]))*' ',end='|   ')
            print(tableau_valide[i][2]+ (16-len(tableau_valide[i][2]))*' ',end='|   ')
            print(tableau_valide[i][3]+ (16-len(tableau_valide[i][3]))*' ',end='|   ')

            print(tableau_valide[i][4]+ (16-len(tableau_valide[i][4]))*' ' +'|  ')
            print('\n')
        head=head+1
    print(105*'-')
#=======================================================================================================================================================================================

def  head5_invalide(fichier):
    tableau_valide,tableau_invalide=tableau_val_inval(fichier)     
    head=0
    for i in range(len(tableau_invalide)):
        if head<5:
            for j in range(len(tableau_invalide[i])-2):
                print(tableau_invalide[i][j]+ (16-len(tableau_invalide[i][j]))*' ',end='|   ')
            print(tableau_invalide[i][4]+ (4)*' ',end=' ')
            print('\n')
            head=head+1
    print(193*'-')

#=======================================================================================================================================================================================

def ajourter(fichier):
    tableau_valide,tableau_invalide=tableau_val_inval(fichier) 
    numero=input('donne le numero : \n')
    nom=input('donne le nom :\n')
    prenom=input('donne le prenom\n')
    date=input(' donne la date de naissance \n')
    classe=input('donne la classe \n')
    Note=input('donne les notes ecrit comme suite \n')
    if numero==numero_valide(numero) and nom==nom_valide(nom) and prenom==prenom_valide(prenom) and date==date_valide(date) and classe==class_valide(classe) and Note==note_val(Note): 
        tableau_valide.append([numero,nom,prenom,date,classe,Note])
    else:
        tableau_invalide.append([numero,nom,prenom,date,classe,Note])
    print(tableau_valide)
    print('\n')
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print(tableau_invalide)
#=======================================================================================================================================================================================

def tableau(Liste):
    print('\n')
    for i in range(len(Liste)):
        
        print(' \t {}- {} \t'.format(i+1,Liste[i]))
        print('\n')

#=======================================================================================================================================================================================

def entete1():
    
    print((100)*'-')
    print('|'+"\033[91m"+'Matiere'+"\033[0m"+(15-len('Matiere'))*' '+' |  '+"\033[91m"+'Note de Devoir'+"\033[0m"+(15-len('Note de Devoi'))*' '+' |  '+'Note d examen'+(15-len('Note d examen'))*' '+' |  '+'Moyenne de Devoir'+(15-len('Moyenne de Devoir'))*' '+' |  '+'Moyenne Generale'+(15-len('Moyenne Generale'))*' '+' |  ')
    print((100)*'-')


#=======================================================================================================================================================================================


def affichage_note_valide(fichier):
    tableau_valide,tableau_invalide=tableau_val_inval(fichier) 
    reponse=1
    while reponse==1:
        numero=input('donne le numero de l etudiant pour voir ces notes \n')
        print('---------------')
        print('| ' +  numero+'    |')
        print('---------------')
        entete1()
        a=[]
        a1=[]
        for j in tableau_valide:
            if j[0]==numero:
                a1=j[5::]
                a=((','.join(a1)).replace("\n",'')).replace(',','.').split('#')
                note=[]
                n=len(a)
                c=[]
                for i in a:
                    n1={}
                    if i!='':
                        if '[' in i:
                            c=i.split('[')
                            n1['Matiere']=c[0]
                            if ':' in c[1]:
                                n1['Note de Devoir']=c[1].split(':')[0]
                                n1['Note d examen']=(c[1].split(':')[1][:-1]).replace(']','')
                                s=0
                                if '|' in (c[1].split(':')[0]):
                                    for j in (c[1].split(':')[0]).split('|'):
                                        s=s+float(j)
                                    n1['Moyenne de Devoir']=round(s/len((c[1].split(':')[0]).split('|')),2)
                                else:
                                    s=s+float(c[1].split(':')[0])
                                    n1['Moyenne de Devoir']=s/len((c[1].split(':')[0]).split('|'))
                                n1['moyenne Generale']=round((n1['Moyenne de Devoir']+2*int(n1['Note d examen']))/3,2)
                                note.append(n1)
                                n1={}
                            else:
                                print(' ')
                n2={}
                s=0
                for i in range(len(note)):
                    s=s+note[i]['moyenne Generale']
                n2['moyenne etudiant']=round(s/len(note),2)
                n2
                note.append(n2)              
                note

                for i in range(len(note)-1):
                    print(note[i]['Matiere']+(15-len(note[i]['Matiere']))*' ', end='  |  ')
                    print(note[i]['Note de Devoir']+(15-len(note[i]['Note de Devoir']))*' ', end='  | ')
                    print(note[i]['Note d examen']+(15-len(note[i]['Note d examen']))*' ', end='  |  ')
                    print(str(note[i]['Moyenne de Devoir'])+(15-len(str(note[i]['Moyenne de Devoir'])))*' ', end='   |  ')
                    print(str(note[i]['moyenne Generale'])+(15-len(str(note[i]['moyenne Generale'])))*' ', end='   ')
                    print('\n')
                print('-------------------------------------')
                print("| moyenne etudiant | "+"\033[91m"+str(note[len(note)-1]['moyenne etudiant'])+"\033[0m"+ 4*' '+'       |')
                print('-------------------------------------')
        reponse=int(input('tape 1 pour verifier d autre notes ou une autre chiffre pour quiter '))
#=========================================================================================================================================================
def affiche_5_line(fichier,depart):
    tableau_valide,tab_inv=tableau_val_inval(fichier)
    for i in range(len(tableau_valide)):
        tableau_valide[i][1]=forme_nom(tableau_valide[i][1])
        tableau_valide[i][2]=forme_prenom(tableau_valide[i][2])
        tableau_valide[i][3]=format_date(tableau_valide[i][3])
        tableau_valide[i][4]=forme_classe(tableau_valide[i][4])
    if depart<=len(tableau_valide)-5:
        for i in range(depart,depart+5):

            print('|\t',end='')
            #for j in range(len(tableau_valide[i])-2):
            print(tableau_valide[i][0]+ (16-len(tableau_valide[i][0]))*' ',end='|   ')
            print(tableau_valide[i][1]+ (16-len(tableau_valide[i][1]))*' ',end='|   ')
            print(tableau_valide[i][2]+ (16-len(tableau_valide[i][2]))*' ',end='|   ')
            print(tableau_valide[i][3]+ (16-len(tableau_valide[i][3]))*' ',end='|   ')

            print(tableau_valide[i][4]+ (16-len(tableau_valide[i][4]))*' ' +'|  ')
            
            print('\n')

def pagination_5_ligne(fichier):
    depart=0
    while True:
        choix=input("Afficher les 5 lignes suivantes (s), les 5 lignes précédentes (p), ou quitter (q) ?\n ")
        if choix=='s':
            depart+=5
            entete()
            affiche_5_line(fichier,depart)
        elif choix=='p':
            entete()
            depart-=5
            affiche_5_line(fichier,depart)
        elif choix=='q':
            break
        else:
            print('choix invalide')


#=======================================================================================================================================================================================


def autre_pagination_5_ligne(fichier):
    tableau_valide,tableau_invalide=tableau_val_inval(fichier) 
    maxe=int(input('taper 1 comme suivant ou 0 comme precedent :\n'))
    entete()
    k=maxe
    while maxe==1 or maxe==0:
        for i in range(len(tableau_valide)):
            tableau_valide[i][1]=forme_nom(tableau_valide[i][1])
            tableau_valide[i][2]=forme_prenom(tableau_valide[i][2])
            tableau_valide[i][3]=format_date(tableau_valide[i][3])
            tableau_valide[i][4]=forme_classe(tableau_valide[i][4])
            #tableau_valide[i][5]=(tableau_valide[i][6].replace("#",' '))
        head=0
        if (k-1)*5<= len(tableau_valide)-5:
            for i in range((k-1)*5,len(tableau_valide)):
                if head<5:
                    print('|\t',end='')
                    #for j in range(len(tableau_valide[i])-2):
                    print(tableau_valide[i][0]+ (16-len(tableau_valide[i][0]))*' ',end='|   ')
                    print(tableau_valide[i][1]+ (16-len(tableau_valide[i][1]))*' ',end='|   ')
                    print(tableau_valide[i][2]+ (16-len(tableau_valide[i][2]))*' ',end='|   ')
                    print(tableau_valide[i][3]+ (16-len(tableau_valide[i][3]))*' ',end='|   ')

                    print(tableau_valide[i][4]+ (16-len(tableau_valide[i][4]))*' ' +'|  ')
                    
                    print('\n')
                head=head+1

            maxe=int(input('taper 1 comme suivant ou 0 comme precedent :\n'))
            k=k+1
#=======================================================================================================================================================================================

def autre_pagination_n_ligne(fichier):
    tableau_valide,tableau_invalide=tableau_val_inval(fichier) 
    n=int(input('donner le nombre de ligne dont vous voulez paginer :\n'))
    maxe=int(input('taper 1 comme suivant ou 0 comme precedent :\n'))
    
    entete()
    k=maxe
    while maxe==1 or maxe==0:
        for i in range(len(tableau_valide)):
            tableau_valide[i][1]=forme_nom(tableau_valide[i][1])
            tableau_valide[i][2]=forme_prenom(tableau_valide[i][2])
            tableau_valide[i][3]=format_date(tableau_valide[i][3])
            tableau_valide[i][4]=forme_classe(tableau_valide[i][4])
            #tableau_valide[i][5]=(tableau_valide[i][6].replace("#",' '))
        head=0
        if (k-1)*n<= len(tableau_valide)-n:
            for i in range((k-1)*n,len(tableau_valide)):
                if head<n:
                    print('|\t',end='')
                    #for j in range(len(tableau_valide[i])-2):
                    print(tableau_valide[i][0]+ (16-len(tableau_valide[i][0]))*' ',end='|   ')
                    print(tableau_valide[i][1]+ (16-len(tableau_valide[i][1]))*' ',end='|   ')
                    print(tableau_valide[i][2]+ (16-len(tableau_valide[i][2]))*' ',end='|   ')
                    print(tableau_valide[i][3]+ (16-len(tableau_valide[i][3]))*' ',end='|   ')

                    print(tableau_valide[i][4]+ (16-len(tableau_valide[i][4]))*' ' +'|  ')
                    print('\n')
                head=head+1
            maxe=int(input('taper 1 comme suivant ou 0 comme precedent :\n'))
            k=k+1
#=======================================================================================================================================================================================

def moyenne_etudiant(numero,fichier):
    tableau_valide,tableau_invalide=tableau_val_inval(fichier) 
    a=[]
    a1=[]
    for j in tableau_valide:
        if j[0]==numero:
            a1=j[5::]
            a=((','.join(a1)).replace("\n",'')).replace(',','.').split('#')
            note=[]
            n=len(a)
            c=[]
            for i in a:
                n1={}
                if i!='':
                    if '[' in i:
                        c=i.split('[')
                        n1['Matiere']=c[0]
                        if ':' in c[1]:
                            n1['Note de Devoir']=c[1].split(':')[0]
                            n1['Note d examen']=(c[1].split(':')[1][:-1]).replace(']','')
                            s=0
                            if '|' in (c[1].split(':')[0]):
                                for j in (c[1].split(':')[0]).split('|'):
                                    s=s+float(j)
                                n1['Moyenne de Devoir']=round(s/len((c[1].split(':')[0]).split('|')),2)
                            else:
                                s=s+float(c[1].split(':')[0])
                                n1['Moyenne de Devoir']=s/len((c[1].split(':')[0]).split('|'))
                            n1['moyenne Generale']=round((n1['Moyenne de Devoir']+2*int(n1['Note d examen']))/3,2)
                            note.append(n1)
                            n1={}
                        else:
                            print(' ')
            n2={}
            s=0
            for i in range(len(note)):
                s=s+note[i]['moyenne Generale']
            n2['moyenne etudiant']=round(s/len(note),2)
            n2
            note.append(n2)  
            return note            

#=======================================================================================================================================================================================

def moyenne_de_chaq_etudiant_selon_numero(fichier):
    tableau_valide,tableau_invalide=tableau_val_inval(fichier) 
    note=[]
    N=[]
    n={}
    for i in range(len(tableau_valide)):
        note=moyenne_etudiant(tableau_valide[i][0],fichier)
        n['Numero']=tableau_valide[i][0]
        n['moyenne etudiant']=note[len(note)-1]['moyenne etudiant']
        N.append(n)
        n={}
    N_trier=sorted(N,key=lambda d: d["moyenne etudiant"],reverse=True)

    return N_trier[1::]
#=======================================================================================================================================================================================

def affichage_5_premier(fichier):
    Moyenne=moyenne_de_chaq_etudiant_selon_numero(fichier)
    print('------------------------------------------')
    print("| " +"Numero"+ (15-len("NUmero"))*' ',end='  | ')
    print("Moyenne etudiant"+(15-len("Moyenne etudiant"))*' '+'   | ')
    print('------------------------------------------')
    head=0
    for i in range(len(Moyenne)):
        if head<5:
            print("| " +Moyenne[i]["Numero"]+ (15-len(Moyenne[i]["Numero"]))*' ',end='  | ')
            print(str(Moyenne[i]['moyenne etudiant'])+(15-len(str(Moyenne[i]["moyenne etudiant"])))*' '+ '    | ')
        head+=1

#=======================================================================================================================================================================================

def affiche():
    print("╔═══════════════════════════════════════════════════════════╗")
    print("║                          menu                             ║")
    print("╠═══════════════════════════════════════════════════════════╣")
    print("║   1. Affichage d'information                              ║")
    print("║      a. Valide                                            ║")
    print("║      b. Invalide                                          ║")
    print("║      c. Notes Valide                                      ║")
    print("║      d. sortir                                            ║")
    print("║   2. Affichage d'information par numero                   ║")
    print("║   3. Affichage des 5 premiers elements                    ║")
    print("║      a. Valide                                            ║")
    print("║      b. Invalide                                          ║")
    print("║      c. sortir                                            ║")
    print("║   4. Ajouterer une information                            ║")
    print("║   5. afficher les 5 premier de la classe                  ║")
    print("║   6. Paginer par 5 ligne                                  ║")
    print("║   7. Paginez par le nombre de ligne de votre choix        ║")
    print("║   8. Quitter                                              ║")
    print("╚═══════════════════════════════════════════════════════════╝")
#=======================================================================================================================================================================================


def menu(fichier):
    affiche()
    while True:
        try:
            choix=int(input('saisissez votre choix dans le menu \n'))
            if choix==1:
                ch=input('    . saisissez votre choix\n')
                if ch=='a':
                    affichage_valide(fichier)
                    affiche()
                elif ch=='b':                    
                    affichage_invalide(fichier)
                    affiche()
                elif ch=='c':
                    affichage_note_valide(fichier)
                    affiche()
                elif ch=='d':
                    print('Au revoir!')
                    break
                else:
                    print('choix invalide ')
            elif choix==2:
                recherche_by_num(fichier)
                affiche()
            elif choix==3:
                ch1=input('saisissez votre choix \n')
                if ch1=='a':
                    head5_valide(fichier)
                    affiche()
                elif ch1=='b':
                    head5_invalide(fichier)
                    affiche()
                elif ch1=='c':
                    print('Au revoir !')
                    break
                else:
                    print('choix invalide')
            elif choix==4:
                ajourter(fichier)
                affiche()
            elif choix==5:
                affichage_5_premier(fichier)
                affiche()
            elif choix==6:
                pagination_5_ligne(fichier)
                affiche()
            elif choix==7:
                pagination_n_ligne(fichier)
                affiche()
            elif choix==8:
                print('Au revoir !')
                break
            else:
                print('choix invalide')
        except ValueError:
            print('Entrer invalide saisie a nouveau ')

#==========================================================================================================================================================================================





    

