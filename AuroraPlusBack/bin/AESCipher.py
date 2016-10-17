from __future__ import print_function
from __future__ import print_function
import base64
import hashlib
import os

from Crypto import Random
from Crypto.Cipher import AES

BS = 16
key = hashlib.md5('peter!').hexdigest()[:BS]
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s: s[:-ord(s[len(s)-1:])]


class AESCipher:
    def __init__(self, key):
        self.key = self.trans(key)

    def encrypt(self, raw):
        raw = pad(raw)
        iv = Random.new().read(AES.block_size)
        print (type(key))
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.urlsafe_b64encode(iv + cipher.encrypt(raw))

    def decrypt(self, enc):
        enc = base64.urlsafe_b64decode(enc.encode('utf-8'))
        iv = enc[:BS]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return unpad(cipher.decrypt(enc[BS:]))

    def trans(self, key):
        return hashlib.md5(key).hexdigest()[:BS]


if __name__ == "__main__":
    ciper = AESCipher('peter!hjkortlrhjb')
    encrypted = ciper.encrypt('hello!')
    decrypted = ciper.decrypt(encrypted)

    print ('encrypted {0} , decrypted: {1}'.format(encrypted, decrypted))

