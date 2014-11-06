#! /usr/bin/python
from Crypto.Cipher import DES3
from Crypto import Random
import base64

#3DES CBC PKCS7
BS= DES3.block_size
MODE = DES3.MODE_CBC
pad = lambda  s:s+(BS-len(s)%BS)*chr(BS-len(s)%BS)
unpad =lambda s:s[:-ord(s[-1])]

#encrypt
def enc(key,p):
	iv = Random.new().read(BS)
	cipher=DES3.new(key,MODE,iv)

	p=pad(p)
	c=cipher.encrypt(p)
	msg = iv+c
	return base64.b64encode(msg)

def dec(key,msg):
	msg=base64.b64decode(msg)
	iv = msg[:BS]
	decipher=DES3.new(key,MODE,iv)
	p = unpad(decipher.decrypt(msg[BS:]))
	return p

def main():
		key=Random.new().read(16)#2*8 bytes
		p='DES3 test'
		msg =enc(key,p)
		print dec(key,msg)

if __name__=='__main__':
		main()
