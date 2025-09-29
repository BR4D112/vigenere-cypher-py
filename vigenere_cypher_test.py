import unittest
from vigenere_cypher import vigenere_cipher

class TestVigenereCipher(unittest.TestCase):

    def test_encrypt(self):
        self.assertEqual(vigenere_cipher("HELLO", "CLAVE", "encrypt"), "JPLGS")
        self.assertEqual(vigenere_cipher("WORLD", "CLAVE", "encrypt"), "YZRGH")
        self.assertEqual(vigenere_cipher("MUNDO", "CLAVE", "encrypt"), "OFNYS")

    def test_decrypt(self):
        self.assertEqual(vigenere_cipher("JPLGS", "CLAVE", "decrypt"), "HELLO")
        self.assertEqual(vigenere_cipher("YZRGH", "CLAVE", "decrypt"), "WORLD")
        self.assertEqual(vigenere_cipher("OFNYS", "CLAVE", "decrypt"), "MUNDO")

    def test_invalid_parameters(self):
        with self.assertRaises(ValueError):
            vigenere_cipher("HELLO", "KEY1", "encrypt")
        with self.assertRaises(ValueError):
            vigenere_cipher("HELLO", "", "encrypt")
        with self.assertRaises(ValueError):
            vigenere_cipher("HELLO", "KEY", "invalid_mode")

if __name__ == '__main__':
    unittest.main()