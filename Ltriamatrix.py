row=4;col=4
M=[[1,2,3,1,],[4,3,2,1],[4,3,2,6],[1,2,7,4]]
sum1=0
for i in range(row):
    for j in range(col):
        if i+j<(row-1):
            M[i][j]=0
        print(M[i][j],end=" ")
    print()
