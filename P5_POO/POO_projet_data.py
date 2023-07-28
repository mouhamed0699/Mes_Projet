# nous allons transformer nos programmes en POO

class Validation:
    def __init__(self,valeure):
        self.valeur=valeure
    # la fonction va verifier si un nom est valide
    def numero_valide(self):
        Maj=['A','B','C','D','E','F','G','H','I','J','K','L','M','N',
             'O','P','Q','R','S','T','U','V','W','X','Y','Z']
        chiffre=["0","1","2","3","4","5","6","7","8","9"]
        s=''
        if len(self.valeur)==7:
            for i in range(len(self.valeur)):        
                if self.valeur[i] in chiffre or self.valeur[i] in Maj:
                    s=s+self.valeur[i]  
            if s==self.valeur:
                return self.valeur
    # la fonction non_valide regarde la validité d'un non
    def nom_valide(self):
        s=0
        if "a"<=self.valeur[0]<="z" or "A"<=self.valeur[0]<="Z":
            for i in range(len(self.valeur)):
                if "a"<=self.valeur[0]<="z" or "A"<=self.valeur[0]<="Z":
                    s=s+1
            if s>=2:
                return self.valeur
    # la fonction prenom_valide regarde la validité d'un prenom
    def prenom_valide(self):
        s=0
        if "a"<=self.valeur[0]<="z" or "A"<=self.valeur[0]<="Z":
            for i in range(len(self.valeur)):
                if "a"<=self.valeur[0]<="z" or "A"<=self.valeur[0]<="Z":
                    s=s+1
            if s>=3:
                return self.valeur
    # cette fonction ci-dessus met une date sous cette format 00-00-0000
    def format_date(self):
        d=''
        c=[]
        for i in self.valeur:
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
    # cette fonction ci-dessus permet de regarder la valider d'une date
    def date_valide(self):
        import datetime
        self.valeur=self.format_date()
        date_format='%d-%m-%Y'
        try :
            date_valide=datetime.datetime.strptime(self.valeur,date_format)
        except ValueError:
            #print('date invalide',date)
            return ' '
        return self.valeur    
    def class_valide(self):
        if self.valeur[0] in ["3","5","6","4"] and self.valeur[len(self.valeur)-1] in ["A","B"]:
            return self.valeur   
    #-----------------------------------------
    def note_val(self):
        L=[]
        t=[]
        d=[]
        k=[]
        new_note=[]
        L=self.valeur.split("#")
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
            return self.valeur
    #------------------------------------------
    def forme_prenom(self):
        d=''
        for i in self.valeur:
            if i==' ':
                d=d+''
            else:
                d=d+i
        return d
    #----------------------------------
    def forme_nom(self):
        d=''
        for i in self.valeur:
            if i==' ':
                d=d+''
            else:
                d=d+i
        return d
    #-----------------------------------------
    def forme_classe(self):
        d=''
        for i in self.valeur:
            if i==' ':
                d=d+''
            else:
                d=d+i
        return d
    #----------------------------------------

class Affichage:
    def __init__(self,fichier):
        self.fichier=fichier
        self.depart=0
        self.numero=''
    # la fonction tab_val_inval nous retourn un tableau contenant les ligne dont toutes ses informations sont valide et tableau contenant le contraire
    def tableau_val_inval(self):
        count_line=0
        tableau_valide=[]
        tableau_invalide=[]
        with open(self.fichier,'r') as f:
            for line in f:
                if count_line>=1:
                    x=line.split(',')
                    if Validation(x[1]).numero_valide()==x[1] and Validation(x[2]).nom_valide()==x[2] and Validation(x[3]).prenom_valide()==x[3] and Validation(x[4]).date_valide()==Validation(x[4]).format_date()  and Validation(x[5]).class_valide()==x[5] and Validation(x[6]).note_val()==x[6]: 
                        tableau_valide.append(x[1::])
                    else:
                        tableau_invalide.append(x[1::])
                        
                count_line+=1
        return tableau_valide,tableau_invalide
    def entete(self):
    
        print((105)*'-')
        print('|\t'+"\033[91m"+'Numero'+"\033[0m"+(16-len('Numero'))*' '+'|   '+"\033[91m"+'Nom'+"\033[0m"+(16-len('Nom'))*' '+'|   '+"\033[91m"+'Prenom'+"\033[0m"+(16-len('Prenom'))*' '+'|   '+"\033[91m"+'Date de Naissance'+"\033[0m"+(16-len('Date de Naissance'))*' '+'|   '+"\033[91m"+'Classe'+"\033[0m"+(16-len('Classe'))*' '+'|   ')
        print((105)*'-')
        
    def affichage_valide(self):
        self.entete()
        tableau_valide,tableau_invalide=self.tableau_val_inval()
        
        for i in range(len(tableau_valide)):
            tableau_valide[i][1]=Validation(tableau_valide[i][1]).forme_nom()
            tableau_valide[i][2]=Validation(tableau_valide[i][2]).forme_prenom()
            tableau_valide[i][3]=Validation(tableau_valide[i][3]).format_date()
            tableau_valide[i][4]=Validation(tableau_valide[i][4]).forme_classe()
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

    def affichage_invalide(self):
        tableau_valide,tableau_invalide=self.tableau_val_inval()
        for i in range(len(tableau_invalide)):
            for j in range(len(tableau_invalide[i])-1):
                print(tableau_invalide[i][j]+ (16-len(tableau_invalide[i][j]))*' ',end='|   ')
            print(tableau_invalide[i][5]+ (4)*' ',end=' ')
            print('\n')
        print(193*'-')   
    def recherche_by_num(self):
        numero=input('donner un numero :\n')
        tableau_valide,tableau_invalide=self.tableau_val_inval() 
        for i in range(len(tableau_valide)):
            if tableau_valide[i][0]==numero:
                print(tableau_valide[i])
    def entete1(self):
        
        print((100)*'-')
        print('|'+"\033[91m"+'Matiere'+"\033[0m"+(15-len('Matiere'))*' '+' |  '+"\033[91m"+'Note de Devoir'+"\033[0m"+(15-len('Note de Devoi'))*' '+' |  '+'Note d examen'+(15-len('Note d examen'))*' '+' |  '+'Moyenne de Devoir'+(15-len('Moyenne de Devoir'))*' '+' |  '+'Moyenne Generale'+(15-len('Moyenne Generale'))*' '+' |  ')
        print((100)*'-')
    def affichage_note_valide(self):
        tableau_valide,tableau_invalide=self.tableau_val_inval() 
        reponse=1
        while reponse==1:
            numero=input('donne le numero de l etudiant pour voir ces notes \n')
            print('---------------')
            print('| ' +  numero+'    |')
            print('---------------')
            self.entete1()
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
    def affiche_5_line(self):
        tableau_valide,tab_inv=self.tableau_val_inval()
        for i in range(len(tableau_valide)):
            tableau_valide[i][1]=Validation(tableau_valide[i][1]).forme_nom()
            tableau_valide[i][2]=Validation(tableau_valide[i][2]).forme_prenom()
            tableau_valide[i][3]=Validation(tableau_valide[i][3]).format_date()
            tableau_valide[i][4]=Validation(tableau_valide[i][4]).forme_classe()
        if self.depart<=len(tableau_valide)-5:
            for i in range(self.depart,self.depart+5):

                print('|\t',end='')
                #for j in range(len(tableau_valide[i])-2):
                print(tableau_valide[i][0]+ (16-len(tableau_valide[i][0]))*' ',end='|   ')
                print(tableau_valide[i][1]+ (16-len(tableau_valide[i][1]))*' ',end='|   ')
                print(tableau_valide[i][2]+ (16-len(tableau_valide[i][2]))*' ',end='|   ')
                print(tableau_valide[i][3]+ (16-len(tableau_valide[i][3]))*' ',end='|   ')

                print(tableau_valide[i][4]+ (16-len(tableau_valide[i][4]))*' ' +'|  ')
                
                print('\n')

    def pagination_5_ligne(self):
        self.depart=0
        while True:
            choix=input("Afficher les 5 lignes suivantes (s), les 5 lignes précédentes (p), ou quitter (q) ?\n ")
            if choix=='s':
                self.depart+=5
                self.entete()
                self.affiche_5_line()
            elif choix=='p':
                self.entete()
                self.depart-=5
                self.affiche_5_line()
            elif choix=='q':
                break
            else:
                print('choix invalide')
    def moyenne_etudiant(self):
        tableau_valide,tableau_invalide=self.tableau_val_inval() 
        a=[]
        a1=[]
        for j in tableau_valide:
            if j[0]==self.numero:
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
    def moyenne_de_chaq_etudiant_selon_numero(self):
        tableau_valide,tableau_invalide=self.tableau_val_inval() 
        note=[]
        N=[]
        n={}
        for i in range(len(tableau_valide)):
            self.numero=tableau_valide[i][0]
            note=self.moyenne_etudiant()
            n['Numero']=tableau_valide[i][0]
            n['moyenne etudiant']=note[len(note)-1]['moyenne etudiant']
            N.append(n)
            n={}
        N_trier=sorted(N,key=lambda d: d["moyenne etudiant"],reverse=True)

        return N_trier[1::]
    #=======================================================================================================================================================================================

    def affichage_5_premier(self):
        Moyenne=self.moyenne_de_chaq_etudiant_selon_numero()
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
    def affiche(self):
        print("╔═══════════════════════════════════════════════════════════╗")
        print("║                          menu                             ║")
        print("╠═══════════════════════════════════════════════════════════╣")
        print("║   1. Affichage d'information                              ║")
        print("║      a. Valide                                            ║")
        print("║      b. Invalide                                          ║")
        print("║      c. Notes Valide                                      ║")
        print("║      d. sortir                                            ║")
        print("║   2. Affichage d'information par numero                   ║")
        print("║   3. afficher les 5 premier de la classe                  ║")
        print("║   4. Paginer par 5 ligne                                  ║")
        print("║   5. Quitter                                              ║")
        print("╚═══════════════════════════════════════════════════════════╝")
    def menu(self):
        self.affiche()
        while True:
            try:
                choix=int(input('saisissez votre choix dans le menu \n'))
                if choix==1:
                    while True:
                        ch=input('    . saisissez votre choix\n')
                        if ch=='a':
                            self.affichage_valide()
                            self.affiche()
                        elif ch=='b':                    
                            self.affichage_invalide()
                            self.affiche()
                        elif ch=='c':
                            self.affichage_note_valide()
                            self.affiche()
                        elif ch=='d':
                            print('Au revoir!')
                            break
                        else:
                            print('choix invalide ')
                elif choix==2:
                    self.recherche_by_num()
                    self.affiche()
                elif choix==3:
                    self.affichage_5_premier()
                    self.affiche()
                elif choix==4:
                    self.pagination_5_ligne()
                    self.affiche()
                elif choix==5:
                    print('Au revoir !')
                    break 
                else:
                    print('choix invalide')
            except ValueError:
                print('Entrer invalide saisie a nouveau ')
# cette instruction ci-dessous permet de d'afficher le menu
Affichage('Donnees_Projet_Python_DataC5(2).csv').menu()
