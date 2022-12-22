l1 = [11, 45, 8, 11, 23, 45, 23, 45, 89]
dict={}
for i in l1:
    count=0
    for j in l1:
        if(i==j):
            count=count+1
    dict[i]=count

print(dict)
