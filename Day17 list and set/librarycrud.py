books=[]
while True:
    print("----eLibaray----")
    print("1:Addbooks\n2:showBooks\n3:Updatebook\n4:Deletebook\n5:Exit")
    choice=int(input("Enter choice number="))
    if choice==1:
        title=input("Enter book title=").capitalize()
        if title not in books:
            books.append(title)
            print(f"{title} Book Added Succesfully!!")
        else:
            print(f"{title} Book is already exits so add another book!!")
    elif choice==2:
        if len(books)==0:
            print("No books available try again")
        else:
            print("Available books are=",books)
    elif choice==3:
        pass
    elif choice==4:
        pass
    elif choice==5:
        print("Thanks for using our Services!!")
        break
