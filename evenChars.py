str = "PYnative"
print(f"Original string is {str}")
print("Printing only even index chars")

#for data in list(str):
#     index=list(str).index(data)
#     id=index/2
#     if id-int(id) == 0:
#         print(data)
#     else:
#         pass
#even_index=[list(str).index(data) for data in list(str) if list(str).index(data)%2 == 0 ]
#print(even_index)

even_index=[data for data in range(0,len(str),2)]

even_chars = [char for char in list(str) if str.index(char)%2==0]
for data in even_chars :
     print(data)
