# #Left Incrimental Pyramid
# count=int(input("Enter row count="))
# for i in range(count):
#     for j in range(i+1):
#         print("*",end="")
#     print()




#Right Incrimental Pyramid
count=int(input("Enter row count="))
for i in range(count):
    for k in range(i):
        print(end=" ")

    for j in range(count,i,-1):
        print("*",end="")
    print()



#Hill-Incrimental Pyramid


#Hill decrimental Pyramid
count=int(input("Enter row count="))
for i in range(count):
    for k in range(i):
        print(end=" ")

    for j in range(count,i,-1):
        print("*",end="")
    print()