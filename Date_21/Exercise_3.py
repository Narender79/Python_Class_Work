sam = [11, 45, 8, 23, 14, 12, 78, 45, 89]
x=slice(0,3)
y=slice(3,6)
z=slice(6,9)
temp=[]
dum=[]
res=[]
for i in sam[x]:
    temp.append(i)
print("Chunk  1:",temp)
temp.reverse()
print("After reversing it:",temp)
for j in sam[y]:
    dum.append(j)
print("Chunk  2:",dum)
dum.reverse()
print("After reversing it:",dum)
for z in sam[z]:
    res.append(z)
print("Chunk  2:",res)
res.reverse()
print("After reversing it:",res)