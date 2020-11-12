import pandas as pd

from klang import klang_encrypt
from caesar_cipher import caeser_cipher_encrypt

class encryptClass:
    def __init__(self, msg):
        self.msg = msg
        print(f'Message "{self.msg}" successfully read')
    
    def print_msg(self):
        print(self.msg)

    def klang_encrypt(self):
        print(klang_encrypt(self.msg))
    
    def caeser_cipher_encrypt(self, s):
        print(caeser_cipher_encrypt(self.msg, s))

    def run(self, s=1):
        self.print_msg()
        self.klang_encrypt()
        self.caeser_cipher_encrypt(s)


encrypt = encryptClass('oie')
encrypt.run()



