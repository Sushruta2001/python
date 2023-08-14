a = int(input("Enter a number"))

match a:
    case 50:
        print("The number is 50")
    case 100:
        print("The number is 100")
    
    case _ if(a!=200):
        print("The number is not 200")
    case _ if(a!=300):
        print("The number is not 300")

    case _:
        print("The number is nothing but",a)




        # OUTPUT
        # Enter a number50
        # The number is 50

        # Enter a number100
        # The number is 100.

        # Enter a number200
        # The number is not 300
