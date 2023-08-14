import time
timestamp=time.strftime("%H:%M:%S")
print("The time is:", timestamp)
hour=time.strftime("%H")
minute=time.strftime("%M")
second=time.strftime("%S")
if(hour>"6" and hour<="12"):    
    print("Good morning sir")
if(hour>"12" and hour<="23" and minute<="59"):
    print("good evening sir")




    # OUTPUT
    # The time is: 16:04:06
    # good evening sir