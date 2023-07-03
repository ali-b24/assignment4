def kmm(a,b):
    m=0
    n=0
    j=abs(a*b)+1
    if abs(a)>abs(b):
        m=abs(a)
    else:
        m=abs(b)
    for i in range (m,j):
        if i%a==0 and i%b==0:
            n=i
            break
    return(n)

a=int(input("Please enter first number:"))
b=int(input("Please enter second number:"))
if a<1 or b<1:
    print("try again later!")
    exit()
    
s=kmm(a,b)
print(s)