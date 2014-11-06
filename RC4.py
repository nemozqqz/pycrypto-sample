#! /usr/bin/python
from Crypto.Cipher import ARC4
from Crypto.Hash import SHA256
from Crypto import Random

def enc(key,p):
		return ARC4.new(key).encrypt(p)

def dec(key,msg):
		return ARC4.new(key).decrypt(msg)

def main():
		key = 'very long key'
		p = 'RC4 test hehehe'
		nonce=Random.new().read(16)
		key +=nonce
		key = SHA256.new(key).digest() #key is no more than 256bytes

		print dec(key,enc(key,p))

if __name__=='__main__':
		main()

