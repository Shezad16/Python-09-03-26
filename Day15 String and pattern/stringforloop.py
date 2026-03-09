#Iterate string
name="ItVedant"
# for i in name:
#     print(i)


#Reverse of string
# print("reverse string=",name[::-1])


# #OR

# newstr=""
# for i in name:
#     newstr=i+newstr
# print(newstr)



#Write a new string to Check whether their is vovel or not
# without_vov=""
# for i in name:
#     if i not in "aeiouAEIOU":
#         without_vov=without_vov+i

# print(without_vov)




#WAP to print number of occurances of entered character from any strings

# str=input("Enter a string=")
# char=input("Enter Caharacter=")
# count=0
# for i in str:
#     if char==i:
#         count+=1

# print(f"{char} character count into {str} is {count}")



#WAP to print number of occurances of entered character and word from any strings

str=input("Enter String=")
chkstr=input("Enter character/word to find and show count=")
count=0
check=""
for i in range(len(str)):
    # print(i,str[i])
    k=i
    for i in range(len(chkstr)):
        try:
            check+=str[k]
            k+=1
        except:
            None
    if check==chkstr:
        count+=1
    check=""

if count!=0:
    print(f"{chkstr} found in {str} and count={count}")
else:
    print(f"{chkstr} not found in {str}")