def mul_tab():
    for i in range(1, m+1):
        for j in range(1, n+1):
            print(i*j , end='\t')
            j = j+1
        print("")
        i=i+1



n = int(input("enter length: "))
m= int(input("enter width: "))


mul_tab()

