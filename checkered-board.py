def checker_board():
    for j in range(m):
        for i in range(n):
            if j%2 == 0:
                if i%2 == 0:
                    print("*" , end="")
                else:
                    print("#" , end="")
            else:
                if i%2 == 0:
                    print("#" , end="")
                else:
                    print("*" , end="")           
        print("")
    
n = int(input("enter length: "))
m = int(input("enter width: "))

checker_board()