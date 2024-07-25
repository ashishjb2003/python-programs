row=5;col=4
M=[[1,2,3,1,],[4,3,2,1],[4,3,2,6],[1,2,7,4],[1,3,5,7]]
maxrs=0;maxrsi=-1
for i in range (row):
    crs=0
    for j in range (col):
        crs = crs+M[i][j]
    if crs>maxrs:
        maxrs=crs
        maxrsi=i
print(maxrs,maxrsi)
