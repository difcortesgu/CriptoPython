from aes.aes import AES
from queue import Queue
import os

class AES_PRBG():
    def __init__(self):
        self.counter = 0
        self.bits = Queue(maxsize=128)
        self.key = b'\x96\x07\xC8\x9D\x88\xC9\xC3\xC7\x53\xFE\x95\x5E\x09\xE0\x37\xBB'
        self.IV = b'\x03\x72\xCE\x45\x62\xFD\x49\xC3\x59\xC3\x14\x43\x7B\x3C\x95\xFA'

    def next_bit(self):
        if self.bits.empty():
            m = bytes(self.counter) + b'0' * (16 - len(bytes(self.counter)))
            self.counter = 
            cypher = AES(self.key)
            c = cypher.encrypt_block(m)
            c = int(c.hex(), 16) ^ int(self.IV.hex(), 16)
            for b in bin(int(c.hex(), 16))[2:]:
                self.bits.put(b)
        return self.bits.get()

    def next_n_bits(self, n):
        a = ""
        for x in range(n):
            a += self.next_bit()
        return a


# gen = AES_PRBG()

# for x in range(10):
#     print(gen.next_n_bits(5))