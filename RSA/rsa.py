import math

def gcd_ext(a,b):
    if b == 0:
        return (a, 1, 0)
    (d_, x_, y_) = gcd_ext(b, a % b)
    return (d_, y_, (x_ - math.floor(a / b) * y_)) 

def inverse_Zn(a, n):
    d,x,y = gcd_ext(a, n)
    return x

a = 10
m = 3571
for x in range(m):
    if (a * x) % m == 1:
        print(x)

d, x, y = gcd_ext(m, a)
print(y)