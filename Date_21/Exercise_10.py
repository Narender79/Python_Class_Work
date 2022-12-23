sample_list = [87, 45, 41, 65, 94, 41, 99, 94]
temp=[]
for i in sample_list:
    if i not in temp:
        temp.append(i)
print(temp)
print(tuple(temp))
print(min(temp))
print(max(temp))