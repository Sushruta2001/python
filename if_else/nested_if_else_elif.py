a = int(input("enter the value of a "))
print(a)

if(a>0):
    if(a<=10):
        print("The number is between 0 and 10")
    elif(a>10 and a<=20):
        print("The number is between 10 and 20")
    elif(a>20 and a<=30):
        print("The number is between 20 and 30")
    else:
        print("The number is greater than 30")

else:
    print("The number is negative")



    # output

# enter the value of a 12
# 12
# The number is between 10 and 20