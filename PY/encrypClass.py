'''
Script com a classe encryptClass
'''

# Packages
import pandas as pd
import logging

# Encryption functions
from klang import klang_encrypt
from caesar_cipher import caeser_cipher_encrypt

# Log config
LOG_FORMAT = "%(asctime)-24s [%(filename)s:%(lineno)d] \
    %(levelname)-6s %(message)s"
logging.basicConfig(filename='PY/logs/logs.log',
                    filemode='a',
                    format=LOG_FORMAT,
                    level=logging.DEBUG)

class encryptClass:
    def __init__(self, msg):
        self.msg = msg
        print(f'Message "{self.msg}" successfully read')
        logging.info(f'Message "{self.msg}" successfully read')
    
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



