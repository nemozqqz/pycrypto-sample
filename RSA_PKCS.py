#! /usr/bin/python

#public key crypto standard #1
#
#use openssl to generate the public & private key
#command:
#	openssl genrsa -out private_rsa.pem	1024
#	openssl rsa -in private_rsa.pem -pubout -out public_rsa.pem
#(default e is 65537(0x10001))
#
#the command below can be used to read key information
#	openssl asn1parse -in private_rsa.pem -inform pem

from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

def enc(pubkey,msg):
		ekey = RSA.importKey(open(pubkey).read())
		cipher = PKCS1_OAEP.new(ekey)
		ciphertext = cipher.encrypt(msg)
		return ciphertext

def dec(prikey,ctext):
		dkey = RSA.importKey(open(prikey).read())
		cipher = PKCS1_OAEP.new(dkey)
		msg = cipher.decrypt(ctext)
		return msg

def main():
		pubkey = 'public_rsa.pem'
		prikey = 'private_rsa.pem'

		msg = 'RSA PKCS encrytion test'
		print dec(prikey,enc(pubkey,msg))

if __name__=='__main__':
		main()
