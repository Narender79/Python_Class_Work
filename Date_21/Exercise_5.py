fl= [2, 3, 4, 5, 6, 7, 8]
sl = [4, 9, 16, 25, 36, 49, 64]
res=[]
for i in fl:
    tup=()
    dum=[]
    for j in sl:
        if i==j**(0.5):
            dum.append(i)
            dum.append(j)
            tup=tuple(dum)
    res.append(tup)
print(res)    
