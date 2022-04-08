def chess():
    a = int(input("Row?\n"))
    b = int(input("Col?\n"))
    for i in range (a):
        if i % 2 == 0:
            for j in range (b):
                if j %2 ==0:
                    print ("🟨",end = " ")
                else:
                    print ("🟩",end = " ")
        # a = a-1
            print ("\n")
            
        else:
            for j in range (b):
                if j %2 ==0:
                    print ("🟩",end = " ")
                else:
                    print ("🟨",end = " ")
            print ("\n")
        
chess ()