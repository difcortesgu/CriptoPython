def string_to_binary(s):
    res = ""
    for c in s:
        aux = bin(ord(c))[2:]
        res += ("0" * (8-len(aux))) + aux
    return res

def string_to_hex(s):
    res = ""
    for c in s:
        aux = hex(ord(c))[2:]
        res += ("0" * (2-len(aux))) + aux
    return res

def binary_to_hex(s):
    return hex(int(s, 2))[2:]

def hex_to_binary(s):
    b = bin(int(s, 16))[2:]
    return ("0" * ((len(s)*4) - len(b)) ) + b

def sum_zn(numbers, n):
    res = 0
    for x in numbers:
        res = (res + x) % n
    return res

def add_padding(s:str) -> str:
    l = bin(len(s))[2:]
    l = ("0" * (128 - len(l))) + l

    s += "1"
    s += "0" * (896 - ((len(s) % 1024) % 896))

    return s + l

def right_shift(s, n):
    return s >> n

def cycle_shift(s, n):
    a = s >> n
    b = (s << (64 - n)) % 2**64
    return a | b

def ch(x, y, z):
    return (x & y) ^ (~x & z) 

def maj(x, y, z):
    return (x & y) ^ (x & z) ^ (y & z)

def SIGMA0(x):
    return cycle_shift(x, 28) ^ cycle_shift(x, 34) ^ cycle_shift(x, 39)

def SIGMA1(x):
    return cycle_shift(x, 14) ^ cycle_shift(x, 18) ^ cycle_shift(x, 41)

def sigma0(x):
    return cycle_shift(x, 1) ^ cycle_shift(x, 8) ^ right_shift(x, 7)

def sigma1(x):
    return cycle_shift(x, 19) ^ cycle_shift(x, 61) ^ right_shift(x, 6)

def compress(a ,b, c, d, e, f, g, h, Kt, Wt):
    T1 = sum_zn([h, SIGMA1(e), ch(e,f,g),Kt, Wt], 2**64)
    T2 = sum_zn([SIGMA0(a), maj(a,b,c)], 2**64)
    h = g
    g = f
    f = e
    e = sum_zn([d, T1], 2**64)
    d = c
    c = b
    b = a
    a = sum_zn([T1, T2], 2**64)
    return (a,b,c,d,e,f,g,h)

def sha512(s):
    s = add_padding(s)
    n_blocks = int(len(s) / 1024)
    H = H0
    for i in range(n_blocks):
        Mi = s[i*1024:(i+1)*1024]
        W = [ int(Mi[i*64:(i+1)*64], 2) for i in range(16) ]
        for t in range(16,80):
            W.append( sum_zn([sigma1(W[t-2]), W[t-7], sigma0(W[t-15]), W[t-16]], 2**64))
        previousH = H
        for t in range(80):
            H = compress(*H, K[t], W[t])
        nextH = []
        for h, ph in zip(H, previousH):
            nextH.append(sum_zn([h, ph], 2**64))
        H = tuple(nextH)
    hash = ""
    for x in H:
        aux = bin(x)[2:]
        pad = "0" * (64 - len(aux))
        hash += (pad + aux)
    return hash

def sha512n(s, n):
    for x in range(n):
        s = sha512(s)
    return s

H0 = (
    0x6a09e667f3bcc908, 0xbb67ae8584caa73b, 0x3c6ef372fe94f82b, 0xa54ff53a5f1d36f1,
    0x510e527fade682d1, 0x9b05688c2b3e6c1f, 0x1f83d9abfb41bd6b, 0x5be0cd19137e2179
)
K = (
    0x428a2f98d728ae22, 0x7137449123ef65cd, 0xb5c0fbcfec4d3b2f, 0xe9b5dba58189dbbc,
    0x3956c25bf348b538, 0x59f111f1b605d019, 0x923f82a4af194f9b, 0xab1c5ed5da6d8118,
    0xd807aa98a3030242, 0x12835b0145706fbe, 0x243185be4ee4b28c, 0x550c7dc3d5ffb4e2,
    0x72be5d74f27b896f, 0x80deb1fe3b1696b1, 0x9bdc06a725c71235, 0xc19bf174cf692694,
    0xe49b69c19ef14ad2, 0xefbe4786384f25e3, 0x0fc19dc68b8cd5b5, 0x240ca1cc77ac9c65,
    0x2de92c6f592b0275, 0x4a7484aa6ea6e483, 0x5cb0a9dcbd41fbd4, 0x76f988da831153b5,
    0x983e5152ee66dfab, 0xa831c66d2db43210, 0xb00327c898fb213f, 0xbf597fc7beef0ee4,
    0xc6e00bf33da88fc2, 0xd5a79147930aa725, 0x06ca6351e003826f, 0x142929670a0e6e70,
    0x27b70a8546d22ffc, 0x2e1b21385c26c926, 0x4d2c6dfc5ac42aed, 0x53380d139d95b3df,
    0x650a73548baf63de, 0x766a0abb3c77b2a8, 0x81c2c92e47edaee6, 0x92722c851482353b,
    0xa2bfe8a14cf10364, 0xa81a664bbc423001, 0xc24b8b70d0f89791, 0xc76c51a30654be30,
    0xd192e819d6ef5218, 0xd69906245565a910, 0xf40e35855771202a, 0x106aa07032bbd1b8,
    0x19a4c116b8d2d0c8, 0x1e376c085141ab53, 0x2748774cdf8eeb99, 0x34b0bcb5e19b48a8,
    0x391c0cb3c5c95a63, 0x4ed8aa4ae3418acb, 0x5b9cca4f7763e373, 0x682e6ff3d6b2b8a3,
    0x748f82ee5defb2fc, 0x78a5636f43172f60, 0x84c87814a1f0ab72, 0x8cc702081a6439ec,
    0x90befffa23631e28, 0xa4506cebde82bde9, 0xbef9a3f7b2c67915, 0xc67178f2e372532b,
    0xca273eceea26619c, 0xd186b8c721c0c207, 0xeada7dd6cde0eb1e, 0xf57d4f7fee6ed178,
    0x06f067aa72176fba, 0x0a637dc5a2c898a6, 0x113f9804bef90dae, 0x1b710b35131c471b,
    0x28db77f523047d84, 0x32caab7b40c72493, 0x3c9ebe0a15c9bebc, 0x431d67c49c100d4c,
    0x4cc5d4becb3e42b6, 0x597f299cfc657e2a, 0x5fcb6fab3ad6faec, 0x6c44198c4a475817
)