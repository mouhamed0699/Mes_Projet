b=input("donner une phrase : \n")
c="0123456789"
d="abcdefghij"
A="abc"
AA="ABC"
B="def"
BB="DEF"
C="ghi"
CC="GHI"
D="jkl"
DD="JKL"
E="mno"
EE="MNO"
F="pqrs"
FF="PQRS"
G="tuv"
GG="TUV"
H="wxyz"
HH="WXYZ"
codage=""
for i in range(len(b)):
    if i<len(b)-1:
        for j in range(len(d)):
            if b[i]==c[j] :
                codage=codage+d[j]
        
        for j in range(len(A)):
            if (b[i]==A[j] or b[i]==AA[j])and b[i+1] in "ABCabc":
                codage=codage+(j+1)*'2' +'0'
            elif b[i]==A[j] or b[i]==AA[j] :
                codage=codage+(j+1)*'2'
            else:
                codage=codage+""
                
        for j in range(len(B)):
            if (b[i]==B[j] or b[i]==BB[j])and b[i+1] in "DEFdef":
                codage=codage+(j+1)*'3' +'0'
            elif b[i]==B[j] or b[i]==BB[j]:
                codage=codage+(j+1)*'3'      
            else:
                codage=codage+"" 

        for j in range(len(C)):
            if (b[i]==C[j] or b[i]==CC[j])and b[i+1] in "GHIghi":
                codage=codage+(j+1)*'4' +'0'
            elif b[i]==C[j] or b[i]==CC[j]:
                codage=codage+(j+1)*'4'   
            else:
                codage=codage+""
                
        for j in range(len(D)):
            if (b[i]==D[j] or b[i]==DD[j])and b[i+1] in "JKLjkl":
                codage=codage+(j+1)*'5' +'0'
            elif b[i]==D[j] or b[i]==DD[j]:
                codage=codage+(j+1)*'5'  
            else:
                codage=codage+""
        for j in range(len(E)):
            if (b[i]==E[j] or b[i]==EE[j])and b[i+1] in "mnoMNO":
                codage=codage+(j+1)*'6' +'0'
            elif b[i]==E[j] or b[i]==EE[j] :
                codage=codage+(j+1)*'6'  
            else:
                codage=codage+""
        for j in range(len(F)):
            if (b[i]==F[j] or b[i]==FF[j])and b[i+1] in "PQRSpqrs":
                codage=codage+(j+1)*'7' +'0'
            elif b[i]==F[j] or b[i]==FF[j]:
                codage=codage+(j+1)*'7'
            else:
                codage=codage+""

        for j in range(len(G)):
            if (b[i]==G[j] or b[i]==GG[j])and b[i+1] in "TUVtuv":
                codage=codage+(j+1)*'8' +'0'
            elif b[i]==G[j] or b[i]==GG[j]:
                codage=codage+(j+1)*'8'  
            else:
                codage=codage+""
                
        for j in range(len(H)):
            if (b[i]==H[j] or b[i]==HH[j])and b[i+1] in "WXYZwxyz":
                codage=codage+(j+1)*'9' +'0'
            elif b[i]==H[j] or b[i]==HH[j]:
                codage=codage+(j+1)*'9'
            else:
                codage=codage+""           
        if b[i]==" ":
            codage=codage+"00"
        if b[i] not in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 ":
            codage=codage+b[i]
    else:
        for j in range(len(d)):
            if b[i]==c[j] :
                codage=codage+d[j]    
        for j in range(len(A)):
            if (b[i]==A[j] or b[i]==AA[j]):
                codage=codage+(j+1)*'2' 
        for j in range(len(B)):
            if (b[i]==B[j] or b[i]==BB[j]):
                codage=codage+(j+1)*'3' 
        for j in range(len(C)):
            if (b[i]==C[j] or b[i]==CC[j]):
                codage=codage+(j+1)*'4' 
        for j in range(len(D)):
            if (b[i]==D[j] or b[i]==DD[j]):
                codage=codage+(j+1)*'5' 
        for j in range(len(E)):
            if (b[i]==E[j] or b[i]==EE[j]):
                codage=codage+(j+1)*'6'
        for j in range(len(F)):
            if (b[i]==F[j] or b[i]==FF[j]):
                codage=codage+(j+1)*'7' 
        for j in range(len(G)):
            if (b[i]==G[j] or b[i]==GG[j]):
                codage=codage+(j+1)*'8'
        for j in range(len(H)):
            if (b[i]==H[j] or b[i]==HH[j]):
                codage=codage+(j+1)*'9' 
        if b[i]==" ":
            codage=codage+"00"
        if b[i] not in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 ":
            codage=codage+b[i]           
print("la forme code de cette phrase est : \n",codage)