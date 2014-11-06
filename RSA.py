#! /usr/bin/python

#use openssl to generate the public & private key
#command:
#	openssl genrsa -out private_rsa.pem	1024
#	openssl rsa -in private_rsa.pem -pubout -out public_rsa.pem
#(default e is 65537(0x10001))
#
#the command below can be used to read key information
#	openssl asn1parse -in private_rsa.pem -inform pem


#IMPORTANT IMPORTANT IMPORTANT
#this is a version of pure RSA,NO PADDING!!!.
#Msg should LESS than modulus
#For real application,you need to split and pad plain text.
#see RSA_PKCS.py
from Crypto.PublicKey import RSA

def enc(pubkey,msg):
		ekey = RSA.importKey(open(pubkey).read())
		ciphertext = ekey.encrypt(msg,1)
#the second parameter in encrypt() is used for compatibility.it will be ignored
		return ciphertext

def dec(prikey,ctext):
		dkey = RSA.importKey(open(prikey).read())
		msg = dkey.decrypt(ctext)
		return msg

def main():
		pubkey = 'public_rsa.pem'
		prikey = 'private_rsa.pem'

		msg = 'RSA encrytion test'
		print dec(prikey,enc(pubkey,msg))

if __name__=='__main__':
		main()

