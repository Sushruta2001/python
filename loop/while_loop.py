a = 5
while (a > 0):
  print(a)
  a = a - 1


# 5
# 4
# 3
# 2
# 1



x = 5
while (x > 0):
    print(x)
    x = x - 1
else:
    print("x is 0")

# 5
# 4
# 3
# 2
# 1
# x is 0



while True:
  number = int(input("Enter a positive number: "))
  print(number)
  if not number > 0:
    break