import math
from this import d
def delta():
    d =b*b-4*a*c

    if d ==0 :

        x=(-b + math.sqrt(delta))

        print("Moadele Yek javab darad. X=",x)

    elif d<0:

        print("Moadele javabe haghighi nadarad!")

    else :    

        x1=(-b + math.sqrt(delta))/(2*a)

        x2=(-b - math.sqrt(delta))/(2*a)

        print("Moadele 2 javab darad.\n X1= ",x1, "\nX2= " , x2)

a = int(input("Please Enter a: "))

b = int(input("Please Enter b: "))

c = int(input("Please Enter c: "))

delta()

