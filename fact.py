def comp_int(p,t,r):
    amount=p*(pow((1+r/100),t))
    comp_int=amount-p
    return comp_int
p=int(input("enter the principal amount:"))
t=int(input("enter the principal time:"))
r=int(input("enter the principal rate:"))
comp_int(p,t,r)
print(comp_int(p,t,r))
