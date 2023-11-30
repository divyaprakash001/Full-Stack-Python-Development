marks=[12,54,98,99,100,1,17,87]
# index=0
# for mark in marks:
#     if index==3:
#         print("harry",index)
#     index+=1
#     print(mark)

# use of enumerate function
# for index, mark in enumerate(marks):
#     if index==3:
#         print("harry",index)
#     print(mark)

for index, mark in enumerate(marks,start=1): # start=1 means take the mark number 3 not index 3
    if index==3:
        print("harry",index)
    print(mark)