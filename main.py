import unittest
from SHA import sha512
from PRBG import test_estadisticos as te

if __name__ == '__main__':
    # x = int('0123456789ABCDEF',16)
    # ans = sha512.SIGMA0(x)
    # ans_b = bin(ans)[2:]
    # ans_h = sha512.binary_to_hex(ans_b)
    # print('Binario: ',ans_b)
    # print('Hexadecimal:',ans_h)


    m = 'Introduccion a la criptografia y seguridad de la informacion.'
    m = sha512.string_to_binary(m)
    c = sha512.sha512n(m, 2)    
    print(sha512.binary_to_hex(c))


    # s = '0123456789ABCDEF0123456789ABCDEF0123456789ABCDEF0123456789ABCDEF'
    # b = sha512.hex_to_binary(s)
    # tf = te.test_frecuencia(b)
    # ts = te.test_serial(b)
    # tp = te.test_poker(b,3)
    # tc = te.test_de_corrido(b)
    # ta = te.test_de_autocorrelation(b, 8)

    # print('test de frequencia', tf)
    # print('test serial', ts)
    # print('test de poker', tp)
    # print('test de corrido', tc)
    # print('test de autocorrelation', ta)



