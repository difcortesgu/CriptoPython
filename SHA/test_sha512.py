import unittest
import sha512
import hashlib

class TestSHA512Methods(unittest.TestCase):

    def test_string_to_binary(self):
        s = "farid %2+$" 
        self.assertEqual(sha512.string_to_binary(s), "01100110011000010111001001101001011001000010000000100101001100100010101100100100")

    def test_string_to_hex(self):
        s = "farid %2+$" 
        self.assertEqual(sha512.string_to_hex(s), "66617269642025322b24")

    def test_binary_to_hex(self):
        b = "01100110011000010111001001101001011001000010000000100101001100100010101100100100"
        h = "66617269642025322b24"
        self.assertEqual(h, sha512.binary_to_hex(b))

    def test_hex_to_binary(self):
        b = "01100110011000010111001001101001011001000010000000100101001100100010101100100100"
        h = "66617269642025322b24"
        self.assertEqual(b, sha512.hex_to_binary(h))

    def test_sum_zn(self):
        numbers = [ 0b10010100, 0b10110101 ]
        n = 2**8
        self.assertEqual(sha512.sum_zn(numbers, n), 0b01001001)

    def test_add_padding(self):
        s = "110101001"
        s_padded = sha512.add_padding(s)
        self.assertEqual(len(s_padded) % 1024, 0)
        self.assertEqual(s_padded[:len(s)], s)
        self.assertEqual(len(s), int(s_padded[-128:], 2))

    def test_right_shift(self):
        s = 0b110101001
        self.assertEqual(0b000110101, sha512.right_shift(s, 3))

    def test_cycle_shift(self):
        s = 0b0000000000000000000000000000000000000000000000000000000110101001
        self.assertEqual(0b0010000000000000000000000000000000000000000000000000000000110101, sha512.cycle_shift(s, 3))
    
    def test_ch(self):
        x = 0b1010010101
        y = 0b1110001010
        z = 0b1010011111
        self.assertEqual(0b1010001010, sha512.ch(x,y,z))

    def test_maj(self):
        x = 0b1010010101
        y = 0b1110001010
        z = 0b1010011111    
        self.assertEqual(0b1010011111, sha512.maj(x,y,z))

    def test_SIGMA0(self):
        s = 0b0000000000000000000000000000000000000000000000000000000110101001
        cxor= 0b0000000000000000000110101111100100010010000000000000000000000000
        self.assertEqual(cxor, sha512.SIGMA0(s))

    def test_SIGMA1(self):
        s =   0b0000000000000000000000000000000000000000000000000000000110101001
        cxor= 0b0000011011001110010000000000000011010100100000000000000000000000
        self.assertEqual(cxor, sha512.SIGMA1(s))

    def test_sigma0(self):
        s =  0b0000000000000000000000000000000000000000000000000000000110101001
        cxor= 0b0010100100000000000000000000000000000000000000000000000011010110
        self.assertEqual(cxor, sha512.sigma0(s))

    def test_sigma1(self):
        s =   0b0000000000000000000000000000000000000000000000000000000110101001
        cxor= 0b0000000000110101001000000000000000000000000000000000110101001110
        self.assertEqual(cxor, sha512.sigma1(s))

    def test_sha512(self):
        H = hashlib.sha512()
        H.update(b'farid')
        expected = H.hexdigest()
        actual = sha512.sha512('farid')
        self.assertEqual( int(expected , 16), int( actual, 2))


if __name__ == '__main__':
    unittest.main()