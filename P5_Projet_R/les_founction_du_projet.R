#_____________________________________________________________________________________________________________________
#|                                      PROJET DE TRAITEMENT DE DONNEES SUR R                                      |
#_____________________________________________________________________________________________________________________

# POJET:
# Récupérer le fichier contenant les données 
# Faites un traitement de ce fichier ensuite mettez les données dans une structure de votre choix
# (liste, tuple, dictionnaire ou une combinaison de ses derniers)
#  Vous devez séparer les données valides et celles non valide (Une ligne est invalide si une
# des informations qu’il contient n’est pas valide) ; pour les ligne invalides vous devez
# garder les informations qui l’on rendu invalide
#  Les différentes données sont :
#  Numéro
# Composé de lettre majuscule et de chiffre
# Sa taille est 7
# Exemple : H5G32YR ou 54YTG5T
#  Prénom
# Commence par une lettre
# Contient au moins 3 lettre
#  Nom
# Commence par une lettre
# Contient au moins 2 lettre
#  Date de naissance
# Doit être une date valide
# Vous devez choisir un format de date et transformer toutes les dates sous ce format
#  Classe
# 6em à 3em plus les lettres A & B
# Vous devez choisir un format de classe et transformer toutes les classes sous ce format
#  Note
# Voici ce que contient la chaine note
# - Les différentes matières sont séparer par dièse #
# - Les notes des matières sont dans des crochets []
# - Les notes de devoir sont séparées par la note d'examen par deux point :
# - Les notes de devoir sont séparées entre eux par une barre verticale |
# Exemple
# Math[12|11:13]#Francais[4|11|8:13]#Anglais[13,5|11:15]#PC[11:9]#SVT[12|9|16|11:12]#HG[10:13]
# Francais[4|11:13]#Anglais[13,5:15]#PC[11:9]#SVT[12|9|16|11:12]#HG[10:13]#Math[12|14,5|11:13]"""

#------------------------------------------------------------------------------------------------------------------
#__________________________________________________________________________________________________________________________
# |                                                 TRAVAIL                                                              |
#__________________________________________________________________________________________________________________________

  
#la fonction numero_valide determine si le numero de l'etudiant est valide 
numero_valide <- function(x){
  s<-''
  if(nchar(x)==7){
    for(i in 1:nchar(x)){
      if (substring(x,i,i) %in% c('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z') |substring(x,i,i) %in% c("0","1","2","3","4","5","6","7","8","9") ){
        s<-paste0(s,substring(x,i,i),sep='')
      }
      
    }
    if(s==x){
      return(TRUE)
    }else{
      return(FALSE)
    }
    
  }else{
    return(FALSE)
  }
  }
# numero_valide <- function(x){
#   if(nchar(x)==7){
#     if(grepl("^[A-Z0-9]+$", x)){
#       return(x)
#     }
#   }
#   return(NULL)
# }
#----------------------------------------------------------------------------------------------------------------
# la fonction numero_valide determine si le nom est valide

nom_valide<-function(x){
  s<-''
  if (grepl("^[A-Za-z]+$",substring(x,1,1))){
    for (i in 1:nchar(x)){
      if (grepl("^[A-Za-z]+$",substring(x,i,i))){
        s<-paste0(s,substring(x,i,i),sep='')
      }
    }
    if(nchar(s)>=2){
      return(TRUE)
    }else{
      return(FALSE)
    }

  }else{
    return(FALSE)
  }

}
#-----------------------------------------------------------------------------------------------------------------
#la fonction prenom_valide determine si un prenom est valide 
prenom_valide <-function(x){
  s<-''
  if (grepl("^[A-Za-z]+$",substring(x,1,1))){
    for (i in 1:nchar(x)){
      if (grepl("^[A-Za-z]+$",substring(x,i,i))){
        s<-paste0(s,substring(x,i,i),sep='')
      }
    }
    if(nchar(s)>=3){
      return(TRUE)
    }else{
      return(FALSE)
    }
    
  }else{
    return(FALSE)
  }
}
#----------------------------------------------------------------------------------------------------------------
# la fonction classe valide cherche si une classe est valide ou pas
classe_valide <-function(x){
  if( substring(x,1,1) %in% c("3","4","6","5") & substring(x,nchar(x),nchar(x)) %in% c("A","B")){
    return(TRUE)
  } else{
    return(FALSE)
  }
}
#---------------------------------------------------------------------------------------------------------------
# la fonction date_valide determine si une date est valide
date_valide <- function(x){
  formats <- c("%d/%m/%Y","%d-%m-%Y","%d:%m:%Y","%d|%m|%Y","%d,%m,%Y","%d %m %Y")
  for (format in formats){
    if(!is.na(as.Date(x,format=format))){
      return(TRUE)
      #return(as.Date(x,format = format))
    }else{
      return(FALSE)
    }
  }
}
#---------------------------------------------------------------------------------------------------------------
#la fonction note_valide determine si une note est valide
note_valide <- function(notes){
  note<-gsub(',','.',notes)
  note<-gsub(' ','',note)
  b=strsplit(note,'#')
  t=TRUE
  for (i in 1:length(b[[1]])){
    c=''
    d=''
    dn=''
    dd=''
    de=0
    c=b[[1]][i]
    if(grepl("\\[", c) & grepl("\\]", c)){
      d=strsplit(c,"\\[")
      dn=strsplit(d[[1]][2],':')
      if(grepl("\\]",dn[[1]][2])){
          de=substr(dn[[1]][2],1,nchar(dn[[1]][2])-1)
          if(!is.na(as.numeric(de)) && 0<=as.numeric(de) & as.numeric(de) <=20){
            if (grepl("\\|",dn[[1]][1])){
              dd=strsplit(dn[[1]][1],'\\|')
              for(j in 1:length(d[[1]])){
                if (!is.na(as.numeric(dd[[1]][j])) && 0<=as.numeric(dd[[1]][j]) & as.numeric(dd[[1]][j]) <=20){
                  t=TRUE
                }else{
                  t=FALSE
                }
              }
            }else{
              if (!is.na(as.numeric(dn[[1]][1])) && 0<=as.numeric(dn[[1]][1]) & as.numeric(dn[[1]][1]) <=20){
                t=TRUE
              }else{
                t=FALSE
              }
            }

          }else{
            t=FALSE
          }

      }else{
        t=FALSE
      }
    }else{
      t=FALSE
    }
  }
  if(t==TRUE){
    return(TRUE)    
  }else{
    return(FALSE)
  }
}
#----------------------------------------------------------------------------------------------------------------
# data contion notre fichier original on l'obtien grace a read.csv
data <- read.csv('fichier.csv',sep=',')
#-----------------------------------------------------------------------------------------------------------------
#grace a nos fonctions on va pouvoir extraire nos donnees valide et invalide 
#et les mettre dans data_valide et dans data_invalide
data_valide <-data.frame(CODE=character(),Numero=character(),Nom=character(),Prénom=character(),
                         Date.de.naissance=character(),Classe=character(),Note=character())
data_invalide<-data.frame(CODE=character(),Numero=character(),Nom=character(),Prénom=character(),
                          Date.de.naissance=character(),Classe=character(),Note=character())
for(i in 1:nrow(data)){
  if(numero_valide(data$Numero[i]) & nom_valide(data$Nom[i]) & prenom_valide(data$Prénom[i]) & date_valide(data$Date.de.naissance[i]) &
     classe_valide(data$Classe[i]) ){
    data_valide[nrow(data_valide)+1,] <-data[i,]
  }else{
    data_invalide[nrow(data_invalide)+1,] <-data[i,]
  }
}
data_valide_finale<-data.frame(CODE=character(),Numero=character(),Nom=character(),Prénom=character(),
                               Date.de.naissance=character(),Classe=character(),Note=character())
for(i in 1:nrow(data_valide)){
  if(note_valide(data_valide$Note[i])){
    data_valide_finale[nrow(data_valide_finale)+1,] <-data_valide[i,]
  }else{
    data_invalide[nrow(data_invalide)+1,]<-data_valide[i,]
  }
}

data_invalide<-data_invalide[complete.cases(data_invalide),]
#______________________________________________________________________________________________
# |         METTTONS MAINTENANT NOS DONNEES VALIDE ET INVALIDE DANS DES FICHIERS CSV        |
#______________________________________________________________________________________________
#
write.csv(data_valide_finale,'fichier_valide.csv') #mettre nos donnees valide dans un fichier csv


write.csv(data_invalide,'fichier_invalide.csv') #mettre nos donnees invalide dans un fichier csv
#______________________________________________________________________________________________
# |         METTTONS MAINTENANT NOS DONNEES VALIDE ET INVALIDE DANS DES FICHIERS  JSON        |
#______________________________________________________________________________________________
#
library(jsonlite)

jsonlite::write_json(data_valide_finale,'fichier_valide.json') #mettre nos donnees valide dans un fichier json


jsonlite::write_json(data_invalide,'fichier_invalide.json') #mettre nos donnees invalide dans un fichier json

#______________________________________________________________________________________________
# |         METTTONS MAINTENANT NOS DONNEES VALIDE ET INVALIDE DANS DES FICHIERS xml        |
#______________________________________________________________________________________________
# POUR LES DONNEES VALIDES
library(xml2)
library(XML)
dat<-xml_new_root('etudiants')
for(i in 1:nrow(data_valide_finale)){
  obs<-xml_add_child(dat,'etudiant')
  xml_add_child(obs,'CODE',data_valide_finale$CODE[i])
  xml_add_child(obs,'Numero',data_valide_finale$Numero[i])
  xml_add_child(obs,'Nom',data_valide_finale$Nom[i])
  xml_add_child(obs,'Prenom',data_valide_finale$Prénom[i])
  xml_add_child(obs,'naissance',data_valide_finale$Date.de.naissance[i])
  xml_add_child(obs,'Classe',data_valide_finale$Classe[i])
  xml_add_child(obs,'Note',data_valide_finale$Note[i])
}
xml2::write_xml(dat,'fichier_valide.xml')

# POUR LES DONNEES INVALIDE
datt<-xml_new_root('etudiants')
for(i in 1:nrow(data_valide_finale)){
  obs<-xml_add_child(datt,'etudiant')
  xml_add_child(obs,'CODE',data_invalide$CODE[i])
  xml_add_child(obs,'Numero',data_invalide$Numero[i])
  xml_add_child(obs,'Nom',data_invalide$Nom[i])
  xml_add_child(obs,'Prenom',data_invalide$Prénom[i])
  xml_add_child(obs,'naissance',data_invalide$Date.de.naissance[i])
  xml_add_child(obs,'Classe',data_invalide$Classe[i])
  xml_add_child(obs,'Note',data_invalide$Note[i])
}
xml2::write_xml(dat,'fichier_invalide.xml')
View(data_invalide)
#______________________________________________________________________________________________
# |         METTTONS MAINTENANT NOS DONNEES VALIDE ET INVALIDE DANS DES FICHIERS xml        |
#______________________________________________________________________________________________
library(yaml)
# Pour les donnees valide
df_va<-as.list(data_valide_finale)
yamal_va<-yaml::as.yaml(df_va)
write(yamal_va,'fichier_valide.yaml')

#POur les donnees invalides
df_inv<-as.list(data_invalide)
yaml_inv<-yaml::as.yaml(df_inv)
write(yaml_inv,'fichier_invalide.yaml')


my_data<-read_yaml('fichier_valide.yaml')
head(my_data)

# data_valide <- data[!is.na(sapply(data$Nom, nom_valide)),]
# data_valide <- data[!is.na(sapply(data$Prénom, prenom_valide)),]
# data_valide <- data[!is.na(sapply(data$Date.de.naissance, date_valide)),]
# data_valide <- data[!is.na(sapply(data$Classe, classe_valide)),]
# data_valide <- data[!is.na(sapply(data$Note, note_valide)),]
# for (i in 1:nrow(data)){
#   if(data$Numero[i]==numero_valide(data$Numero[i]))
# }

# Créer une fonction pour vérifier si une date est valide
# est_date_valide <- function(date) {
#   as.logical(as.Date(date, format = "%m/%d/%Y"))
# }
#
# Créer un exemple de données avec des dates valides et invalides
# donnees <- data.frame(
#   date = c("01/01/2021", "02/31/2021", "03/01/2021", "04/01/2021"),
#   valeur = c(10.5, 9.2, 12.1, 15.7),
#   autre_colonne = c("a", "b", "c", "d")
# )
View(data_valide_finale)
