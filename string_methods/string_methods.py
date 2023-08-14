
a = "Rick is a good boy !!!!!!!!"
print(len(a))       # 27
print(a)            # Rick is a good boy !!!!!!!!
print(a.upper())    #RICK IS A GOOD BOY !!!!!!!!
print(a.lower())    #rick is a good boy !!!!!!!!
print(a.rstrip("!"))    #Rick is a good boy    (trailing ! gets removed)
print(a.replace("good", "bad"))     #Rick is a bad boy !!!!!!!!
print(a.split(" "))     #['Rick', 'is', 'a', 'good', 'boy', '!!!!!!!!']



b = "Hello World"
print(b.capitalize())       #Hello world   (only first letter gets capitalized , rest lower case)
print(len(b))               #11


c = "Rick is a good boy and Rick does good work "
print(c.count("Rick"))      #2  (Rick occurs 2 times in the string)


print(a.endswith("!!!"))        #True (ends with !!!)



str1 = "He is Rick. He is a good boy."
print(str1.find("ishh"))      # -1 ( -1 means false. ishh is not present in the string str1)
# print(str1.index("ishh"))       #error. as ishh is not present
print(str1.index("is"))             #3 . in str1, "is" comes at index 3. 




print(str1.isalnum())               #False.   As it has both uppercase and lowercase characters.



print(str1.isalpha())               #False. As it has  numbers or symbols present.


print(str1.islower())               #False. As it has uppercase letters.


print(str1.isprintable())           #True.

print(str1.isspace())               #False. As it has spaces.



str1 = "Hello World"      
print(str1.istitle())               #True. All starting has capitals

str2 = "Hello world"
print(str2.istitle())               #False. All starting doesnt have capitals

str1 = "My name is Rick" 
print(str1.startswith("My"))        #True. As it starts with the given character

str1 = "My Name Is Rick" 
print(str1.swapcase())              #mY nAME iS rICK . All uppercase changed to lowercase and viceversa.

str1 = "My name is rick. rick loves to eat."        #My Name Is Rick. Rick Loves To Eat.  All starting changed to capitals.
print(str1.title())