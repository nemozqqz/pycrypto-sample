Cryptography lib sample use in PyCrypto

PyCrypto:
	default included in python
	if not,try sudo apt-get install python-crypto
Site:
	https://www.dlitz.net/software/pycrypto/
	https://github.com/dlitz/pycrypto

Used module:
	Crypto.Cipher.AES
	Crypto.Cipher.ARC4
	Crypto.Cipher.DES
	Crypto.Cipher.DES3
	Crypto.Cipher.RSA
	Crypto.Cipher.PKCS1_OAEP

	Crypto.Hash.HMAC
	Crypto.Hash.MD5
	Crypto.Hash.SHA1
	Crypto.Hash.SHA256

	Crypto.Random

Details:
Block crypto working mode is CBC,padding pattern is PKCS#7,iv is random generated.

RSA encryption reads public and private key file (e.g private.pem),you can use openssl to generate the key file.
There is also a full detailed RSA version(raw_rsa.py)

See source codes for more details.



