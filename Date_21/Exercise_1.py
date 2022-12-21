l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]
temp=[]
dum=[]
for i in range(0,len(l1)):
    if i%2!=0:
        temp.append(l1[i])
print("Element at odd-index positions from list one:",temp)
for j in range(0,len(l2)):
    if j%2==0:
        dum.append(l2[j])
print("Element at even-index positions from list two:",dum)

for i in dum:
    temp.append(i)
print("Printing Final third list:",temp)