import itertools
import math

def test_frecuencia(s):
    n = len(s)
    n0 = s.count("0")
    n1 = s.count("1")
    return (n0 - n1)**2 / n

def test_serial(s):
    n = len(s)
    n0 = s.count("0")
    n1 = s.count("1")
 
    n00 = 0
    n01 = 0
    n10 = 0
    n11 = 0
    for i in range(len(s)-1):
        if (s[i:i+2] == '00'):
            n00 += 1
        elif (s[i:i+2] == '01'):
            n01 += 1    
        elif (s[i:i+2] == '10'):    
            n10 += 1
        elif (s[i:i+2] == '11'):
            n11 += 1

    return (4 * (n00**2 + n01**2 + n10**2 + n11**2)  / ( n-1 )) - (2 * (n0**2 + n1**2) / n) + 1

def test_poker(s, m):
    k = math.floor(len(s) / m)
    assert k >= (5 * 2**m), "la cadena es muy corta para que el test sea concluyente"

    n = {}
    for x in itertools.product('01', repeat=m):
        value = ''.join(x)
        n[value] = 0

    for block in [s[i*m:i*m+m] for i in range(k)]:
        n[block] += 1
    
    X = 0
    for x in n.values():
        X += x**2
    return ((2**m/k) * X) - k

def count_n_substrings(s, n):
    counts = {}
    for x in itertools.product('01', repeat=n):
        value = ''.join(x)
        counts[value] = s.count(value)
    return counts

def test_de_corrido(s):
    k = 1
    e = []
    e.append(((len(s) - k + 3) / 2**(k+2)))
    while e[-1] >= 5:
        k += 1
        e.append(((len(s) - k + 3) / 2**(k+2)))
    k -= 1
    e.pop()
    B = {}
    G = {}
    for i in range(1,k+1)[::-1]:
        B['1' * i] = s.count('1' * i) 
        G['0' * i] = s.count('0' * i) 
        # esto es para que solo se cuenten los corridos mas grandes
        s = s.replace('1' * i, ' ')
        s = s.replace('0' * i, ' ')
    X = 0
    for i, ei in enumerate(e):
        b = B['1'*(i+1)]
        g = G['0'*(i+1)]
        X += ((b - ei)**2)/ei
        X += ((g - ei)**2)/ei
    return X

def test_de_autocorrelation(s, d):
    assert d >= 1 and d <= math.floor(len(s) / 2)
    Ad = 0
    for i in range(len(s)-d):
        Ad += int(s[i] != s[i+d])
    return 2 * ((Ad - ((len(s)-d) / 2) ) / ( math.sqrt(len(s)-d) ) )
