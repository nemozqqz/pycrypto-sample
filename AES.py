#! /usr/bin/python

from Crypto import Random
from Crypto.Cipher import AES
import base64


#AES CBC PKCS7
BS = AES.block_size #16 byte
MODE = AES.MODE_CBC
pad = lambda s:s+(BS-len(s)%BS)*chr(BS-len(s)%BS)
unpad = lambda s:s[:-ord(s[-1])] #?padding oracle?


#encrypt
def enc(key,p):
	iv  = Random.new().read(BS)
	cipher = AES.new(key,MODE,iv)

	p = pad(p)
	c = cipher.encrypt(p)
	msg = iv+c

	return base64.b64encode(msg)

#decrypt
def dec(key,msg):
		msg = base64.b64decode(msg)
		iv = msg[:BS]
		decipher = AES.new(key,MODE,iv)
		p = unpad(decipher.decrypt(msg[BS:]))
		return p

def main():
		key = Random.new().read(16)
		p = 'AES test end';
		msg = enc(key,p)

		print dec(key,msg)

if __name__=='__main__':
		main()



