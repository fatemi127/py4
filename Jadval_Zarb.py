i = int(input("i?\n"))
j = int(input("j?\n"))

print("x", end=" ") 

x = 1
while x <= i:
     print(x ,end=" ")
     x += 1

y = 1
while y <= j:
     print("")
     print(y,end=" ")
     z = 1  
     while z <= i:
          print(y*z ,end=" ") 
          z += 1
     y += 1 
print()