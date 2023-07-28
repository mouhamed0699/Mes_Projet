A=['Janvier','Février','Mars','Avril','Mai','Juin','Juillet','Août','Septembre','Octaber','Novenbre','Décembre']
B=['January','February','March','April','May','June','July','Auguste','September','Octaber','Novenber','Décember']
print("le menu francais est")

print("____________________________________________") 
for i in range(0,len(A),3):
    print(A[i]+(len(A[8])-len(A[i]))*" ",end='|')
print("")
print("____________________________________________")
for j in range(1,len(A),3):
    print(A[j]+(len(A[8])-len(A[j]))*" ",end='|')
print("")
print("____________________________________________")
for k in range(2,len(A),3):
    print(A[k]+(len(A[8])-len(A[k]))*" ",end='|')
print("")
print("____________________________________________")
b=int(input("choisir 1 pour le menu françcais ou 0 pour le menu anglais : \n"))
if b==1:
    print("le menu francais est")
    print("____________________________________________") 
    for i in range(0,len(A),3):
        print(A[i]+(len(A[8])-len(A[i]))*" ",end='|')
    print("")
    print("____________________________________________")
    for j in range(1,len(A),3):
        print(A[j]+(len(A[8])-len(A[j]))*" ",end='|')
    print("")
    print("____________________________________________")
    for k in range(2,len(A),3):
        print(A[k]+(len(A[8])-len(A[k]))*" ",end='|')
    print("")
    print("____________________________________________")
elif b==0:
    print("le menu anglais est")
    print("____________________________________________") 
    for i in range(0,len(B),3):
        print(B[i]+(len(B[8])-len(B[i]))*" ",end='|')
              
    print("")
    print("____________________________________________")
    for j in range(1,len(B),3):
        print(B[j]+(len(B[8])-len(B[j]))*" ",end='|')
    print("")
    print("____________________________________________")
    for k in range(2,len(B),3):
        print(B[k]+(len(B[8])-len(B[k]))*" ",end='|')
    print("")
    print("____________________________________________")
else:
    print('vous devez donner 1 pour le menu français ou 0 pour l''anglais')