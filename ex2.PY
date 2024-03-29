import math
a = float(input("saise a:"))
b = float(input("saise b:"))
c = float(input("saise c:"))
def equation(a,b,c):
    delta=((b**2)-4*a*c)
    print("delta = ",delta) 
    if(delta>0):
        r =math.sqrt(delta)
        x1=(-b-r)/2*a
        x2=(-b+r)/2*a
        print(" les deux solutions de  équation est S={",x1,",",x2,"}")
    elif(delta==0):
        x=-b/2*a
        print(" solution de  equation et S={",x,"}")
    else:
        print("il na pas solution de cet equation S={""}")
equation(a,b,c)