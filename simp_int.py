def simp_int(p,t,r):
    simp_int=(p*t*r)/100
    return simp_int
p=int(input("enter the principal amount"))
t=int(input("enter the time"))
r=int(input("enter the rate"))
print("total is",simp_int(p,t,r))

