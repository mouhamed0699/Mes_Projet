import EXERCICE9
EXERCICE9.tableau(['saisir une suite operateur telephonique(Orange,Tigo,Expresso,Promobile)','saisir les information d\'un client','affiche des client de la matrice par operateur','affichage des client d un operateur','Afficher les numéros téléphone d’un client','modifier un numero','ajouter un client','Sortir'])
c=int(input('si vous voulez effectuer une tâche taper la chiffre correspondante : '))

while c in [1,2,3,4,5,6,7,8] :
    if c==1:
        M=EXERCICE9.saisie_operateur()
        print(M)
        EXERCICE9.tableau(['saisir une suite operateur telephonique(Orange,Tigo,Expresso,Promobile)','saisir les information d\'un client','affiche des client de la matrice par operateur','affichage des client d un operateur','Afficher les numéros téléphone d’un client','modifier un numero','ajouter un client','Sortir'])
    elif c==2:
        t=EXERCICE9.saisie_info_client()
        EXERCICE9.file_text(t,'exercice9.txt')
        EXERCICE9.tableau(['saisir une suite operateur telephonique(Orange,Tigo,Expresso,Promobile)','saisir les information d\'un client','affiche des client de la matrice par operateur','affichage des client d un operateur','Afficher les numéros téléphone d’un client','modifier un numero','ajouter un client','Sortir'])
    elif c==3 :
        EXERCICE9.affichage_matx_clients_operateur(t)
        EXERCICE9.tableau(['saisir une suite operateur telephonique(Orange,Tigo,Expresso,Promobile)','saisir les information d\'un client','affiche des client de la matrice par operateur','affichage des client d un operateur','Afficher les numéros téléphone d’un client','modifier un numero','ajouter un client','Sortir'])
    elif c==4:
        EXERCICE9.affichage_client_operatuer(t)
        EXERCICE9.tableau(['saisir une suite operateur telephonique(Orange,Tigo,Expresso,Promobile)','saisir les information d\'un client','affiche des client de la matrice par operateur','affichage des client d un operateur','Afficher les numéros téléphone d’un client','modifier un numero','ajouter un client','Sortir'])
    elif c==5:
        EXERCICE9.affichage_numero_client(t)
        EXERCICE9.tableau(['saisir une suite operateur telephonique(Orange,Tigo,Expresso,Promobile)','saisir les information d\'un client','affiche des client de la matrice par operateur','affichage des client d un operateur','Afficher les numéros téléphone d’un client','modifier un numero','ajouter un client','Sortir'])
    elif c==6:
       t=EXERCICE9.modification(t)
       EXERCICE9.affichage_matx_clients_operateur(t)
       EXERCICE9.tableau(['saisir une suite operateur telephonique(Orange,Tigo,Expresso,Promobile)','saisir les information d\'un client','affiche des client de la matrice par operateur','affichage des client d un operateur','Afficher les numéros téléphone d’un client','modifier un numero','ajouter un client','Sortir'])
    elif c==7:
       EXERCICE9.ajouter(t)
       EXERCICE9.affichage_matx_clients_operateur(t)
       EXERCICE9.tableau(['saisir une suite operateur telephonique(Orange,Tigo,Expresso,Promobile)','saisir les information d\'un client','affiche des client de la matrice par operateur','affichage des client d un operateur','Afficher les numéros téléphone d’un client','modifier un numero','ajouter un client','Sortir'])      

    else:
        exit()
    c=int(input('si vous voulez effectuer une tâche taper la chiffre correspondante : '))
