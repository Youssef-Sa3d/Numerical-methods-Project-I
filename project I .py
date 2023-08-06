import math
from sympy import *
from tabulate import tabulate



a = []
b = []
c = []
fa = []
dfa = []
ga = []
fb = []
fc = []


A = int(input("a = "))
B = int(input("b = "))
X = float(input("X for fixed = "))
tol = pow(10 , -2)
itr = math.log((B-A) / tol) / math.log(2)
n = round(itr)
x = symbols("x")
e = input("f(x) = ")
eq = eval(e)
deq = diff(eq , x)

def f(z):
    return eq.subs(x , z)
def df(z):
    return deq.subs(x , z)

def secant(m,n):
    a.append(m)
    b.append(n)
    fa.append(f(a[0]))
    fb.append(f(b[0]))
    c.append(b[0] - fb[0]*( (b[0] - a[0]) / (fb[0] - fa[0]) ))
    fc.append(f(c[0]))
    
    for i in range(n):
        a.append(b[i])
        b.append(c[i])
        fa.append(f(a[i+1]))
        fb.append(f(b[i+1]))
        c.append(b[i+1] - fb[i+1]*((b[i+1] - a[i+1]) / (fb[i+1] - fa[i+1])))
        fc.append(f(c[i+1]))
        if abs(fc[-1]) < tol:
            break
        else: continue

    
    print("Secant")
    table = {"a": a, "b": b, "c": c, "f(a)": fa, "f(b)": fb, "f(c)": fc}
    print(tabulate(table, headers="keys", tablefmt="fancy_grid", showindex="always"))
    print("Root = " , c[-1])
    
    
    
def modified(m , n):
    a.append(m)
    b.append(n)
    fa.append(f(a[0]))
    fb.append(f(b[0]))
    c.append(b[0] - fb[0]*((b[0] - a[0]) / (fb[0] - fa[0])))
    fc.append(f(c[0]))
    
    for i in range(n):
        if fc[i] < 0  and  fa[i] > 0  and fb[i] < 0 :
            a.append(a[i])
            b.append(c[i])
            fa.append(f(a[i+1]))
            fb.append(f(b[i+1]))
            c.append(b[i+1] - fb[i+1]*((b[i+1] - a[i+1]) / (fb[i+1] - fa[i+1])))
            fc.append(f(c[i+1]))
        elif fc[i] < 0 and fa[i] < 0 and fb[i] > 0 :
            a.append(c[i])
            b.append(b[i])
            fa.append(f(a[i+1]))
            fb.append(f(b[i+1]))
            c.append(b[i+1] - fb[i+1]*((b[i+1] - a[i+1]) / (fb[i+1] - fa[i+1])))
            fc.append(f(c[i+1]))
        elif fc[i] > 0 and fa[i] > 0 and fb[i] < 0 :
            a.append(c[i])
            b.append(b[i])
            fa.append(f(a[i+1]))
            fb.append(f(b[i+1]))
            c.append(b[i+1] - fb[i+1]*((b[i+1] - a[i+1]) / (fb[i+1] - fa[i+1])))
            fc.append(f(c[i+1]))
        elif fc[i] > 0 and fa[i] < 0 and fb[i] > 0 :
            a.append(a[i])
            b.append(c[i])
            fa.append(f(a[i+1]))
            fb.append(f(b[i+1]))
            c.append(b[i+1] - fb[i+1]*((b[i+1] - a[i+1]) / (fb[i+1] - fa[i+1])))
            fc.append(f(c[i+1]))
        
        if abs(fc[-1]) < tol:
            break
        else:
            continue
    
    print("Modified Secant")
    table = {"a": a, "b": b, "c": c, "f(a)": fa, "f(b)": fb, "f(c)": fc}
    print(tabulate(table, headers="keys", tablefmt="fancy_grid", showindex="always"))
    print("Root = ", c[-1])
            
            

def newton(m):
    a.append(m)
    fa.append(f(a[0]))
    dfa.append(df(a[0]))
    
    for i in range(10):
        a.append(a[i] - (fa[i] / dfa[i]))
        fa.append(f(a[i+1]))
        dfa.append(df(a[i+1]))
    
        if abs(fa[-1]) < tol:
            break
        else:
            continue
        
        
    print("Newton Raphson")

    print("df(x) = ", deq)

    table = {"Xi": a, "f(X)": fa, "df(X)": dfa}
    print(tabulate(table, headers="keys", tablefmt="fancy_grid", showindex="always"))
    print("Root = ", a[-1])
    
    

def fixed(m):
    N = int(input("N = "))
    a.append(m)
    fa.append(f(a[0]))
    ga.append(fa[0] + a[0])
    
    for i in range(N-1):
        a.append(ga[i])
        fa.append(f(a[i+1]))
        ga.append(fa[i+1] + a[i+1])
        
        if abs(ga[-1]) < tol:
            break
        else:
            continue

    print("Fixed Point")

    table = {"Xi": a, "f(X)": fa, "g(X)": ga}
    print(tabulate(table, headers="keys", tablefmt="fancy_grid", showindex="always"))
    print("Root = ", ga[-1])
        
    


print("fixed point method, or newton raphson method, or secant method, or modified secant method ")
what = input("Enter the method you want to use: ")
if what == "fixed point method" or what == "fixed point" or what == "fixed":
    fixed(X)
elif what == "newton raphson method" or what == "newton raphson" or what == "newton":
    newton(A)
elif what == "secant method" or what == "secant":
    secant(A, B)
elif what == "modified secant method" or what == "modified secant" or what == "modified":
    modified(A, B)
else:
    print("Error")

    