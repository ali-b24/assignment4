while True:

    a=int(input("Please enter first number:"))
    b=int(input("Please enter number second number:"))

    if a<1 or b<1:
        print("try again later!")
        break
    elif a<b:
        temp=a
        a=b
        b=temp
    while (b!=0):
        c=a%b
        a=b
        b=c
    print(a)