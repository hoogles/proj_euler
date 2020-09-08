#bring in the solution of p008
import numpy as np

def max_prod(x,y):
    mp = 0
    n = len(x)
    i=0
    mi =0
    while i<=(n-y):
        p = 1
        for j in range(i,i+y):
            p *= int(x[j])
        if p>mp:
            mp = p
            mi = i
        i+=1
    return (mp,mi)

#bring in the matrix via text file.
with open('p011.txt', 'r') as f:
    
    l = np.array([[int(num) for num in line.split()] for line in f])
print(l)

 max_hor = 0

max_vert = 0
max_diag = 0
max_diag_flip = 0
mv_xy = [0,0]
mh_xy = [0,0]
md_xy = [0,0]
mdf_xy = [0,0]
hnums = [0,0,0,0]
vnums = [0,0,0,0]
dnums = [0,0,0,0]
dfnums = [0,0,0,0]

for i in range(len(l)):
    diag_l = max_prod(np.diag(np_l,-i),4)
    diag_r = max_prod(np.diag(np_l,i),4)
    diagf_l = max_prod(np.diag(np.fliplr(np_l),k=-i),4)
    diagf_r = max_prod(np.diag(np.fliplr(np_l),k=i),4)
    hor = max_prod(np_l[i],4)
    vert = max_prod(np_l.transpose()[i],4)
    if hor[0]>max_hor:
        max_hor = hor[0]
        mh_xy = [i,hor[1]]
        hnums = [np_l[i][hor[1]],np_l[i][hor[1]+1],np_l[i][hor[1]+2],np_l[i][hor[1]+3]]
        
    if vert[0]>max_vert:
        max_vert = vert[0]
        mv_xy = [vert[1],i]
       
        #vnums = [np_l[vert[1]][i],np_l[vert[1]+1][i],np_l[vert[1]+3][i],np_l[vert[1]+4][i]]
        vnums[0] =   np_l[vert[1]][i]
        vnums[1] =   np_l[vert[1]+1][i]            
        vnums[2] =   np_l[vert[1]+2][i]
        vnums[3] =   np_l[vert[1]+3][i]
    if diag_l[0]>max_diag:
        max_diag = diag_l[0]
        md_xy = [i+diag_l[1],diag_l[1]]
        dnums = [np_l[i+diag_l[1]][diag_l[1]],np_l[i+diag_l[1]+1][diag_l[1]]+1,np_l[i+diag_l[1]+2][diag_l[1]]+2,np_l[i+diag_l[1]+3][diag_l[1]]+3]

    if diag_r[0]>max_diag:
        max_diag= diag_r[0]
        md_xy = [diag_r[1],len(l)-i+diag_r[1]]
        dnums = [np_l[diag_r[1]][len(l)-i+diag_r[1]],np_l[diag_r[1]+1][len(l)-i+diag_r[1]+1],np_l[diag_r[1]+2][len(l)-i+diag_r[1]+2],np_l[diag_r[1]+3][len(l)-i+diag_r[1]+3]]

    if diagf_l[0]>max_diag_flip:
       max_diag_flip = diagf_l[0]
       mdf_xy = [diagf_l[1],len(np_l)-diagf_l[1]-1]
       dfnums = [np_l[diagf_l[1]][len(np_l)-diagf_l[1]-1],np_l[diagf_l[1]+1][len(np_l)-diagf_l[1]-2],np_l[diagf_l[1]+2][len(np_l)-diagf_l[1]-3],np_l[diagf_l[1]+3][len(np_l)-diagf_l[1]-4]]
    if diagf_r[0]>max_diag_flip:
        max_diag_flip= diagf_r[0]
        mdf_xy = [diagf_r[1],len(np_l)-diagf_r[i]-i-1]
        dfnums = [np_l[diagf_r[1]][len(np_l)-diagf_r[i]-i-1],np_l[diagf_r[1]+1][len(np_l)-diagf_r[i]-i-2],np_l[diagf_r[1]+2][len(np_l)-diagf_r[i]-i-3],np_l[diagf_r[1]+3][len(np_l)-diagf_r[i]-i-4]]

max4 = max([max_hor,max_vert,max_diag,max_diag_flip])
if max4==max_hor:
    print(hnums)
elif max4 == max_vert:
    print(vnums)
elif max4 == max_diag:
    print(dnums)
else:
    print(dfnums)
