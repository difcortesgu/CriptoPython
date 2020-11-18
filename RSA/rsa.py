import math

def gcd_ext(a,b):
    if b == 0:
        return (a, 1, 0)
    (d_, x_, y_) = gcd_ext(b, a % b)
    return (d_, y_, (x_ - math.floor(a / b) * y_)) 

def inverso_Zn(a, n):
    d,x,y = gcd_ext(a, n)
    return x

def sistema_ecuaciones(a, n):
    for i in n:
        for j in n:
            d,x,y = gcd_ext(i, j)
            assert d == 1
    N = 1
    for ni in n:
        N *= ni
    x = 0
    for ai, ni in zip(a, n):
        Ni = int(N / ni)
        yi = inverso_Zn(Ni, ni)
        x += (Ni * yi * ai) % N
    return x
n = [2,3,4,5,6,7]
a = [1,1,1,1,1,0]
x = sistema_ecuaciones( a, n)

for ai, ni in zip(a, n):
    print(x % ni, ai)

print(x)

