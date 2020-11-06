def cifrar_cesar(m, k, modulo):
    c = []
    for x in m:
        c.append((x + k) % modulo)
    return c

def descrifrar_cesar(c, k, modulo):
    m = []
    for x in c:
        m.append((x - k) % modulo)
    return m
