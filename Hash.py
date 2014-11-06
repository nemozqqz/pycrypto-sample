#! /usr/bin/python

from Crypto.Hash import HMAC
from Crypto.Hash import MD5
from Crypto.Hash import SHA
from Crypto.Hash import SHA256
from Crypto import Random

def HMAChash(key,msg,mod=MD5): 
		#default hash mod is MD5,SHA and SHA256 are alternative 
		return HMAC.new(key,msg,mod).hexdigest()

def MD5hash(msg):
		return MD5.new(msg).hexdigest()

def SHAhash(msg):
		return SHA.new(msg).hexdigest()

def SHA256hash(msg):
		return SHA256.new(msg).hexdigest()

def main():
		#key = Random.new().read(1024)
		key = 'this is a secret key'
		msg = 'Hash function test end'
		print HMAChash(key,msg)
		print MD5hash(msg)
		print SHAhash(msg)
		print SHA256hash(msg)

if __name__=='__main__':
		main()


