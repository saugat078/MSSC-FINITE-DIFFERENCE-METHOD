# import sympy as sp
from sympy import *
print("\nPlease note the following:")
print("1.The differential equation should be in the form:")
print("y''+ p(x)y'+ q(X)y = r(x)  where p(x), q(x) and r(x) are function of x only\n")

x= symbols('x')
p = sympify(input("Enter the function for p(x): "))
q = sympify(input("Enter the function for q(x): "))
r = sympify(input("Enter the function for r(x): "))
# print(p.subs(x,1))


print(f"The differential equation is :  y'' + {p}y' + {q}y = {r}\n")

print("2.The initials are as y(x0) = a and y(xn) = b")
x0 = int(input("Enter the value for x0: "))
a = float(input("Enter the value for a: "))
xn = int(input("Enter the value for xn: "))
b = float(input("Enter the value for b: "))

n = int(input("\nHow many intervals you want to break your domain? "))
h = (xn-x0)/n

# n = 6
# h = (3-0)/n

# # # Defining the intervals
xs = [i*h for i in range(n+1)]
# print(xs)

px = [p.subs(x,xs[i]) for i in range(1,n)]
qx = [q.subs(x,xs[i]) for i in range(1,n)]
rx = [r.subs(x,xs[i]) for i in range(1,n)]
# print(px)
# qx
# rx


# # # For the equation
y = Function('y')
ys = [y(i) for i in range(n+1)]
# print(ys)

# # # Here the unknowns are 
unknownys = ys[1:n]
# print(unknownys)



# # For the linear equation
Equations = [((ys[i+1]-2*ys[i]+ys[i-1])/h**2 +(px[i-1]*(ys[i+1]-ys[i-1]))/(2*h)+qx[i-1]*ys[i]-rx[i-1]).subs({ys[0]:a,ys[n]:b}) for i in range(1,n)]
# print(Equations[i] for i in range(0,len(Equations)))
print("\nThe equations are:")
for index,item in enumerate(Equations):
    print(f"{index+1}. {item} = 0")
# print(type(Equations))

sol = list(linsolve(Equations,unknownys))
# print(sol)
solnlist = {ys[i+1]:round(sol[0][i],4) for i in range(len(sol[0]))}
print("\nThe solution after solving is:")
print(solnlist)
#  print(sp.solve(x**2 - 1, x))

# print(exp(2))