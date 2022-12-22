first_set = {23, 42, 65, 57, 78, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}
temp=[]
for i in first_set:
    for j in second_set:
        if(i==j):
            temp.append(i)
for k in temp:
    first_set.remove(k)

print("Intersection is:",temp)
print("First Set after removing common element:",first_set)
