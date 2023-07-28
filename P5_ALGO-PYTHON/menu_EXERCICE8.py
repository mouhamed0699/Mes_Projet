import EXERCICE8
tab=[['Mouhammed','Niah','773939841','M2',12,15,18,15],['Mamour','Mbaye','782758349','L3',11,13,18,14],['Fatou','Samb','774502013','TS2',14,5,17,12],['Mami','Ndiaye','709805431','L3',16,17,18,17]]
tab1=EXERCICE8.saisie(tab)
EXERCICE8.file_text(tab1,'exercice8.txt')
EXERCICE8.tableau(['Afficher tout','Trier et Afficher(par ordre decroissante)','Rechercher Selon un Critere(Telephone nom prenom ou classe','modification de notes pour un étudiant choisit par l’utilisateur en donnant lenuméro de téléphone','Sortir'])
c=float(input('Taper 1- pour afficher 2- pour trier 3- pour recher 4-pour modifier et 5- pour sotir : \n'))
while c in [1,2,3,4,5]:
    if c==1:
        EXERCICE8.affichage(tab1)
        
        EXERCICE8.tableau(['Afficher tout','Trier et Afficher(par ordre decroissante)','Rechercher Selon un Critere(Telephone nom prenom ou classe','modification de notes pour un étudiant choisit par l’utilisateur en donnant lenuméro de téléphone','Sortir'])
    elif c==2:
        tab1=EXERCICE8.trier(tab1)
        EXERCICE8.affichage(tab1)
        EXERCICE8.tableau(['Afficher tout','Trier et Afficher(par ordre decroissante)','Rechercher Selon un Critere(Telephone nom prenom ou classe','modification de notes pour un étudiant choisit par l’utilisateur en donnant lenuméro de téléphone','Sortir'])
    elif c==4:
        EXERCICE8.modification(tab1)
        EXERCICE8.affichage(tab1)
    
        EXERCICE8.tableau(['Afficher tout','Trier et Afficher(par ordre decroissante)','Rechercher Selon un Critere(Telephone nom prenom ou classe','modification de notes pour un étudiant choisit par l’utilisateur en donnant lenuméro de téléphone','Sortir'])
    elif c==3:
        EXERCICE8.recherche(tab1)

    else  :
        exit()
    c=float(input('Taper 1- pour afficher 2- pour trier 3- pour recher 4-pour modifier et 5- pour sotir : \n'))
EXERCICE8.file_text(tab1,'exercice8.txt')

