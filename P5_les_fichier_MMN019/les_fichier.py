
from projet_data import* 
import xml.etree.ElementTree as et
import json
import csv
import os
import atexit

#=============================================================================================================================================================
# cette fonction fonction permet de suprimer tous les fichier a la fin du programme
def suprimer_les_fichiers():
    for fichier in ['fichier.xml','fichier.json','new1_valide_fichier.json',
                    'new1_valide_fichier.csv','new1_valide_fichier.xml','new1_invalide_fichier.json',
                    'new1_invalide_fichier.csv','new1_invalide_fichier.xml','new2_valide_fichier.json',
                    'new2_valide_fichier.csv','new2_valide_fichier.xml','new2_invalide_fichier.json',
                    'new2_invalide_fichier.csv','new2_invalide_fichier.xml']:
        if os.path.exists(fichier):
            os.remove(fichier)
            print(f"le {fichier} est suprimé :")
atexit.register(suprimer_les_fichiers)
chemin_csv="Donnees_Projet_Python_DataC5(2).csv"
#===========================================================================================================================================================================
def convertir_csv_en_XML(chemin_csv):
    import csv
    with open(chemin_csv,'r') as f:
        liste_csv=csv.reader(f)
        data=[]
        for liste in liste_csv:
            data.append(liste)
    etudiants=et.Element('etudiants')
    for a in data:
        etudiant=et.SubElement(etudiants,'etudiant');
        code=et.SubElement(etudiant,'CODE')
        code.text=a[0]
        numero=et.SubElement(etudiant,'Numero')
        numero.text=a[1]
        nom=et.SubElement(etudiant,'Nom')
        nom.text=a[2]
        prenom=et.SubElement(etudiant,'Prenom')
        prenom.text=a[3]
        date=et.SubElement(etudiant,'Date')
        date.text=a[4]
        classe=et.SubElement(etudiant,'Classe')
        classe.text=a[5]
        note=et.SubElement(etudiant,'Note')
        note.text=a[6]
    tree=et.ElementTree(etudiants)
    tree.write('fichier.xml')
convertir_csv_en_XML(chemin_csv)
#======================================================================================================================================================================
# pour un fichier xml
def tab_valide_invalide_apartir_xml():
    tree=et.parse('fichier.xml')
    root=tree.getroot()
    donnee=[]
    for eleve in root.findall('etudiant'):
        d={}
        d['Code']=eleve.findtext('Code')
        d['Numero']=eleve.findtext('Numero')
        d['Nom']=eleve.findtext('Nom')
        d['Prenom']=eleve.findtext('Prenom')
        d['Date de naissance']=eleve.findtext('Date')
        d['Classe']=eleve.findtext('Classe')
        d['Note']=eleve.findtext('Note')
        donnee.append(d)
    count_line=0
    tabl_valide=[]
    tabl_invalide=[]
    for line in donnee:
        if count_line>=0:
            if line['Numero']==numero_valide(line['Numero']) and line['Nom']==nom_valide(line['Nom']) and line['Prenom']==prenom_valide(line['Prenom']) and format_date(line['Date de naissance'])==date_valide(line['Date de naissance']) and line['Classe']==class_valide(line['Classe']) and line['Note']==note_val(line['Note']):

                tabl_valide.append(line)
            else:
                tabl_invalide.append(line)
        count_line+=1
    return tabl_valide,tabl_invalide
#==============================================================================================================================================================================
def convertir_csv_en_json(chemin_csv):
    data=[]
    with open(chemin_csv,'r') as fil:
        r=csv.DictReader(fil)
        data=list(r)
    with open('fichier.json','w') as json_file:
        json.dump(data,json_file)

#=============================================================================================================================================================================
# pour un fichier json
def tab_valide_invalide_apartir_json():
    with open('fichier.json','r') as f:
        d=json.load(f)
    data=list(d)
    count_line=0
    tab_valide=[]
    tab_invalide=[]
    for line in data:
        if count_line>=0:
            if line['Numero']==numero_valide(line['Numero']) and line['Nom']==nom_valide(line['Nom']) and line['Prénom']==prenom_valide(line['Prénom']) and format_date(line['Date de naissance'])==date_valide(line['Date de naissance']) and line['Classe']==class_valide(line['Classe']) and line['Note']==note_val(line['Note']):
                
                tab_valide.append(line)
            else:
                tab_invalide.append(line)
        count_line+=1
    return tab_valide,tab_invalide
#====================================================================================================================================

def tableau_val_inval_csv(fichier):
    count_line=0
    tableau_valide=[]
    tableau_invalide=[]
    with open(fichier,'r') as f:
        for line in f:
            if count_line>=1:
                x=line.split(',')
                if numero_valide(x[1])==x[1] and nom_valide(x[2])==x[2] and prenom_valide(x[3])==x[3] and date_valide(x[4])==format_date(x[4])  and class_valide(x[5])==x[5] and note_val(x[6])==x[6]: 
                    tableau_valide.append(x)
                else:
                    tableau_invalide.append(x)
                    
            count_line+=1
    return tableau_valide,tableau_invalide
#==================================================================================================================================================================================
# pour un fichier csv
def mettre_valide_json_invalide_xml(chemin_csv):
    tab_val,tab_inval=tableau_val_inval_csv(chemin_csv)
    with open('new1_valide_fichier.json','w') as file_json:
        json.dump(tab_val,file_json)
    etudiants=et.Element('etudiants')
    for a in tab_inval:
        etudiant=et.SubElement(etudiants,'etudiant')
        code=et.SubElement(etudiant,'CODE')
        code.text=a[0]
        numero=et.SubElement(etudiant,'Numero')
        numero.text=a[1]
        nom=et.SubElement(etudiant,'Nom')
        nom.text=a[2]
        prenom=et.SubElement(etudiant,'Prenom')
        prenom.text=a[3]
        date=et.SubElement(etudiant,'Date')
        date.text=a[4]
        classe=et.SubElement(etudiant,'Classe')
        classe.text=a[5]
        note=et.SubElement(etudiant,'Note')
        note.text=a[6]
    tree=et.ElementTree(etudiants)
    tree.write('new1_invalide_fichier.xml')

#==================================================================================================================================================================================
#pour un fichier csv
def mettre_valide_xml_invalide_json(chemin_csv):
    tab_val,tab_inval=tableau_val_inval_csv(chemin_csv)
    with open('new1_invalide_fichier.json','w') as file_json:
        json.dump(tab_inval,file_json)
    etudiants=et.Element('etudiants')
    for a in tab_val:
        etudiant=et.SubElement(etudiants,'etudiant')
        code=et.SubElement(etudiant,'CODE')
        code.text=a[0]
        numero=et.SubElement(etudiant,'Numero')
        numero.text=a[1]
        nom=et.SubElement(etudiant,'Nom')
        nom.text=a[2]
        prenom=et.SubElement(etudiant,'Prenom')
        prenom.text=a[3]
        date=et.SubElement(etudiant,'Date')
        date.text=a[4]
        classe=et.SubElement(etudiant,'Classe')
        classe.text=a[5]
        note=et.SubElement(etudiant,'Note')
        note.text=a[6]
    tree=et.ElementTree(etudiants)
    tree.write('new1_valide_fichier.xml')

#==================================================================================================================================================================================
# pour un fichier json
def mettre_valide_csv_invalide_xml(chemin_csv):
    convertir_csv_en_json(chemin_csv)
    tab_val,tab_inval=tab_valide_invalide_apartir_json()
    with open('new1_valide_fichier.csv','w') as file:
        writer=csv.writer(file)
        l=[]
        for a in tab_val:
            l.append(a['CODE'])
            l.append(a['Numero'])
            l.append(a['Nom'])
            l.append(a['Prénom'])
            l.append(a['Date de naissance'])
            l.append(a['Classe'])
            l.append(a['Note'])
            writer.writerow(l)
            l=[]
    etudiants=et.Element('etudiants')
    for a in tab_inval:
        etudiant=et.SubElement(etudiants,'etudiant')
        code=et.SubElement(etudiant,'CODE')
        code.text=a['CODE']
        numero=et.SubElement(etudiant,'Numero')
        numero.text=a['Numero']
        nom=et.SubElement(etudiant,'Nom')
        nom.text=a['Nom']
        prenom=et.SubElement(etudiant,'Prenom')
        prenom.text=a['Prénom']
        date=et.SubElement(etudiant,'Date')
        date.text=a['Date de naissance']
        classe=et.SubElement(etudiant,'Classe')
        classe.text=a['Classe']
        note=et.SubElement(etudiant,'Note')
        note.text=a['Note']
    tree=et.ElementTree(etudiants)
    tree.write('new2_invalide_fichier.xml')

#==================================================================================================================================================================================
# pour json
def mettre_valide_xml_invalide_csv(chemin_csv):
    convertir_csv_en_json(chemin_csv)
    tab_val,tab_inval=tab_valide_invalide_apartir_json()
    with open('new1_invalide_fichier.csv','w') as file:
        writer=csv.writer(file)
        l=[]
        for a in tab_inval:
            l.append(a['CODE'])
            l.append(a['Numero'])
            l.append(a['Nom'])
            l.append(a['Prénom'])
            l.append(a['Date de naissance'])
            l.append(a['Classe'])
            l.append(a['Note'])
            writer.writerow(l)
            l=[]
    etudiants=et.Element('etudiants')
    for a in tab_val:
        etudiant=et.SubElement(etudiants,'etudiant')
        code=et.SubElement(etudiant,'CODE')
        code.text=a['CODE']
        numero=et.SubElement(etudiant,'Numero')
        numero.text=a['Numero']
        nom=et.SubElement(etudiant,'Nom')
        nom.text=a['Nom']
        prenom=et.SubElement(etudiant,'Prenom')
        prenom.text=a['Prénom']
        date=et.SubElement(etudiant,'Date')
        date.text=a['Date de naissance']
        classe=et.SubElement(etudiant,'Classe')
        classe.text=a['Classe']
        note=et.SubElement(etudiant,'Note')
        note.text=a['Note']
    tree=et.ElementTree(etudiants)
    tree.write('new2_valide_fichier.xml')
#mettre_valide_csv_invalide_xml(chemin_csv)
#==================================================================================================================================================================================
# pour xml
def mettre_invalide_csv_valide_json():
    tab_val,tab_inval=tab_valide_invalide_apartir_xml()
    with open('new2_invalide_fichier.json','w') as f:
        json.dump(tab_val,f)
    with open('new2_invalide_fichier.csv','w') as file:
        writer=csv.writer(file)
        l=[]
        for a in tab_inval:
            l.append(a['CODE'])
            l.append(a['Numero'])
            l.append(a['Nom'])
            l.append(a['Prénom'])
            l.append(a['Date'])
            l.append(a['Classe'])
            l.append(a['Note'])
            writer.writerow(l)
            l=[]
#=================================================================================================================================================================================
def mettre_valide_csv_invalide_json():
    tab_val,tab_inval=tab_valide_invalide_apartir_xml()
    with open('new2_invalide_fichier.json','w') as f:
        json.dump(tab_inval,f)
    with open('new2_valide_fichier.csv','w') as file:
        writer=csv.writer(file)
        l=[]
        for a in tab_val:
            #l.append(a['CODE'])
            l.append(a['Numero'])
            l.append(a['Nom'])
            l.append(a['Prenom'])
            l.append(a['Date de naissance'])
            l.append(a['Classe'])
            l.append(a['Note'])
            writer.writerow(l)
            l=[]

#==================================================================================================================================================================================
#mettre_valide_csv_invalide_json()
def affiche2():
    print("╠════════════════════════════════════════════════════════════════════════════╣")
    print("║   1. CSV                                                                   ║")
    print("║      a. Mettez les donnees valide en Json et les donnees invalide dans xml ║")
    print("║      b. Mettez les donnees valide en xml et les donnees invalide dans json ║")
    print("║      c. Sortir                                                             ║")
    print("║   2. JSON                                                                  ║")
    print("║      a. Mettez les donnees valide en csv et les donnees invalide dans xml  ║")
    print("║      b. Mettez les donnees valide en xml et les donnees invalide dans csv  ║")
    print("║      c. Sortir                                                             ║")
    print("║   3. XML                                                                   ║")
    print("║      a. Mettez les donnees valide en Json et les donnees invalide dans csv ║")
    print("║      b. Mettez les donnees valide en csv et les donnees invalide dans json ║")
    print("║      c. Sortir                                                             ║")
    print("║   4.Quitter                                                                ║")
    print("╚════════════════════════════════════════════════════════════════════════════╝")
#===================================================================================================================================================================================
def choix_ouverture_mettre_fichier():
    affiche2()
    while True:
        choix=int(input('saisissez votre choix d\'ouverture de fichier \n'))
        if choix==1:
            ch=input('        saisisez votre choix ')
            if ch=='a':
                mettre_valide_json_invalide_xml(chemin_csv)
                
            elif ch=='b':
                mettre_valide_xml_invalide_json
            elif ch=='c':
                print('        Au revoir ! ')
                break
            else:
                print('        choix invalide')
        elif choix==2:
            ch1=input('        saisisez votre choix ')
            if ch1=='a':
                mettre_valide_csv_invalide_xml()
            elif ch1=='b':
                mettre_valide_xml_invalide_csv()
            elif ch1=='c':
                print('         Au revoir !')
                break
            else:
                print('         choix indisponible')
        elif choix==3:
            ch2=input('        saisisez votre choix')
            if ch2=='a':
                mettre_invalide_csv_valide_json()
            elif ch2=='b':
                mettre_valide_csv_invalide_json()
            elif ch2=='c':
                print('        Au revoir !')
                break
            else:
                print('        choix invalide')
        elif choix==4:
            print('Au revoir ! a Bientôt ')
            break
        else:
            print('choix non valide ')

#===================================================================================================================================================================================

choix_ouverture_mettre_fichier()
                






