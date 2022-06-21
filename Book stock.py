

shop={"dbms":20,"os":10,"coa":15}

def add():

    name=str(input("enter the book name: "))

    stock=int(input("enter the number of stocks of:"))

    if name in shop:

          shop[name]=shop[name]+stock

    else:

        shop[name]=stock

def sell():

    name=str(input("enter the book name: "))

    if name in shop:

          stock=int(input("enter the number of stocks of:"))

          shop[name]=shop[name]-stock

    else:

         print("no book with name",name)

def prt():

    print(shop)

flag=0

print("choose any option")

while flag==0:

     print("__________________________________________")

     print("\n\n1.ADD STOCK\n2.SELL\n3.PRINT STOCK\n4.Exit")

     ch=int(input("enter the choice :"))

     if ch==1:

         add()

     elif ch==2:

         sell()

     elif ch==3:

         prt()

     elif ch==4:

          flag=1

          print("\n\n_______________-program exited-________________")

     else :

         print("enter a valid choice")
