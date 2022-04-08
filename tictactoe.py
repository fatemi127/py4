import random
a = [[" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]]

def check():
    if choose == 1:
        name = "PC"
    elif choose == 2:
        name = "Player 2"
    if a[0][0]=="❌"and a[0][1]== "❌" and a [0][2] =="❌":
        print ("Player 1 won!")
    if a[1][0]=="❌"and a[1][1]== "❌" and a [1][2] =="❌":
        print ("Player 1 won!")
    if a[2][0]=="❌"and a[2][1]== "❌" and a [2][2] =="❌":
        print ("Player 1 won!")
    if a[0][0]=="❌"and a[1][0]== "❌" and a [2][0] =="❌":
        print ("Player 1 won!")
    if a[0][1]=="❌"and a[1][1]== "❌" and a [2][1] =="❌":
        print ("Player 1 won!")
    if a[0][2]=="❌"and a[1][2]== "❌" and a [2][2] =="❌":
        print ("Player 1 won!")
    if a[0][0]=="🔵"and a[0][1]== "🔵" and a [0][2] =="🔵":
        print (name," won!")
    if a[1][0]=="🔵"and a[1][1]== "🔵" and a [1][2] =="🔵":
        print (name," won!")
    if a[2][0]=="🔵"and a[2][1]== "🔵" and a [2][2] =="🔵":
        print (name," won!")
    if a[0][0]=="🔵"and a[1][0]== "🔵" and a [2][0] =="🔵":
        print (name," won!")
    if a[0][1]=="🔵"and a[1][1]== "🔵" and a [2][1] =="🔵":
        print (name," won!")
    if a[0][2]=="🔵"and a[1][2]== "🔵" and a [2][2] =="🔵":
        print (name," won!")
    # for idx in range(3):
    #     if a[0][idx] == "❌":
    #         if a[0][idx] == a[1][idx] and a[0][idx] == a[2][idx]:
    #             print ("P1 Won!")
    #     if a[0][idx] == "❌":
    #         if a[idx][0] == a[idx][1] and a[idx][0] == a[idx][2]:
    #             print ("P1 won")

    # for idx in range(3):
    #     if a[0][idx] == "🔵":
    #         if a[0][idx] == a[1][idx] and a[0][idx] == a[2][idx]:
    #             print ("P2 Won!")
    #     if a[0][idx] == "🔵":
    #         if a[idx][0] == a[idx][1] and a[idx][0] == a[idx][2]:
    #             print ("P2 won")       
b = 0
choose = int (input("Choose how many player? For play with PC Enter 1 or for play with another player Enter 2\n"))
if choose == 2:
    while True:
        print ("Player 1:\n")
        while True:
            row = int(input("Row\n"))
            col = int(input("Col\n"))
            if 0<= row <= 2 and 0<= col<=2:
                if a [row][col] == " ":
                    a[row][col] ="❌"
                    break
                else:
                    print("Try Again plz!")
            else:
                print ("Wrong Place! plz try again")
        # check()
        for row in a:
            print(row)
        print ("Player 2:\n")
        while True:
            row = int(input("Row\n"))
            col = int(input("Col\n"))
            if 0<= row <= 2 and 0<= col<=2:
                if a [row][col] == " ":
                    a[row][col] ="🔵"
                    break
                else:
                    print("Try Again plz!")
            else:
                print ("Wrong Place! plz try again")
        check()
        for row in a:
            print(row)
        b = b+1
        print ("toole bazi = ",b)
elif choose == 1:
    while True:
        print ("Player 1:\n")
        while True:
            row = int(input("Row\n"))
            col = int(input("Col\n"))
            if 0<= row <= 2 and 0<= col<=2:
                if a [row][col] == " ":
                    a[row][col] ="❌"
                    break
                else:
                    print("Try Again plz!")
            else:
                print ("Wrong Place! plz try again")
        while True:
            row = random.randint(0,2)
            col = random.randint(0,2)
            if 0<= row <= 2 and 0<= col<=2:
                if a [row][col] == " ":
                    a[row][col] ="🔵"
                    break
            # else:
            #     print ("Wrong Place! plz try again")
        check()
        for row in a:
            print(row)
        b = b+ 1
        print ("toole bazi = ",b)
else:
    print ("Only 1 player or 2 players.")