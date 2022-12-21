li=[34, 54, 67, 89, 11, 43, 94]
x=li[4]
li.remove(li[4])
print("List After removing element at index 4:",li)
li.insert(2,x)
print("List after Adding element at index 2:",li)
li.append(x)
print("List after Adding element at last:",li)