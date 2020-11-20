import math

# ESTO ES EL TEOREMA PERO NO SIRVE EN LOS CASOS GENERALES
# def sistema_ecuaciones(a, n):
#     for i in n:
#         for j in n:
#             d,x,y = gcd_ext(i, j)
#             assert d == 1
#     N = 1
#     for ni in n:
#         N *= ni
#     x = 0
#     for ai, ni in zip(a, n):
#         Ni = int(N / ni)
#         yi = inverso_Zn(Ni, ni)
#         x += (Ni * yi * ai) % N
#     return x

def gcd_ext(a,b):
    if b == 0:
        return (a, 1, 0)
    (d_, x_, y_) = gcd_ext(b, a % b)
    return (d_, y_, (x_ - math.floor(a / b) * y_)) 

def inverso_Zn(a, n):
    d,x,y = gcd_ext(a, n)
    return x if x > 0 else x + n

def resolver(a, b, c):
    g,xg,yg = gcd_ext(a, b)
    assert c % g == 0, "No tiene solución"
    return (xg*int(c/g), yg*int(c/g))

def resolver_sistema(a, n):
    if len(a) == 2:
        g, xg, yg = gcd_ext(n[0], n[1])
        l = int(n[0]*n[1] / g)
        k1, k2 = resolver(n[0], -n[1], a[1]-a[0])
        return (n[0] * k1 + a[0]) % l, l
    else:
        ax, lx = resolver_sistema(a[1:], n[1:]) 
        g, xg, yg = gcd_ext(n[0], lx)
        l = int(n[0]*lx / g)
        k1, k2 = resolver(n[0], -lx, ax-a[0])
        return (n[0] * k1 + a[0]) % l, l

def phi(n): 
	result = n; 
	p = 2; 
	while(p * p <= n): 
		if (n % p == 0): 
			while (n % p == 0): 
				n = int(n / p); 
			result -= int(result / p); 
		p += 1; 
	if (n > 1): 
		result -= int(result / n); 
	return result; 

def fast_exp(b, e, m):
    r = 1
    if 1 & e:
        r = b
    while e:
        e >>= 1
        b = (b * b) % m
        if e & 1: r = (r * b) % m
    return r

# print(power(2, 3272385792339238235, 2375237409232047236321))
# print((2**3272385792339238235) % 2375237409232047236321)

# print(hex(3944386443535457617003026438985303)[2:])

# a = 2212008723594000000
# b = 9682074586145000000
# c = 8020190800000000
# x, y = resolver(a,b,c)
# print( a * x + b * y == c )
# print(x,y)

# print(phi(299421893672399102251119082355330))

# n = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
# a = [1,1,1,1,1,1,1,1,1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]
# x, N = resolver_sistema(a, n)
# for ai, ni in zip(a, n):
#     print(x, "=", ai, "(mod ", ni, ")")
#     assert x % ni == ai

# for x in range(23,698377681, 23):
#     for ai, ni in zip(a, n):
#         if x % ni != ai :
#             break
#     else:
#         print(x)

