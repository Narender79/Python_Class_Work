roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sample_dict = {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}
temp=[]
for i in sample_dict:
    for j in roll_number:
        if(j==sample_dict[i]):
            temp.append(j)
print("After removing unwanted elements from list:",temp)