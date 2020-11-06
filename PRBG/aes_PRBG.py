from aes.aes import AES
from queue import Queue
import os

class AES_PRBG():
    def __init__(self):
        self.counter = 0
        self.bits = Queue(maxsize=128)
        self.key = os.urandom(16)

    def next_bit(self):
        if self.bits.empty():
            m = bytes(self.counter) + b'0' * (16 - len(bytes(self.counter)))
            self.counter += 1
            cypher = AES(self.key)
            c = cypher.encrypt_block(m)
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