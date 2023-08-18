
def name(*name):
  print(name[0],name[1])

  name("Rick", " Kayal")







def name(**name):
 
  print("Hello,", name["fname"], name["lname"])


name(fname="Rick", lname="Kayal")

# OUTPUT
# Hello, Rick Kayal
