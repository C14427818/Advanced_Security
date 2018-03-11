#!/usr/bin/python
from Crypto.PublicKey import RSA
from Crypto import Random

print "Lab 4 RSA Algorithm"

'''
STEPS IN CODE BUT ALL DONE IN RSA LIBRARY OF PYTHON

#1 TWO PRIME NUMBERS P AND Q

def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')
    
    #2 N =PQ CALCULATE MODULUS
    n = p * q

    #3 CALCULATE TOTIENT
    tot = (p-1) * (q-1)

    #4CHOOSE INT COPRIME TO T
    e = random.randrange(1, tot)

    g = gcd(e, tot)
    while g != 1:
        e = random.randrange(1, tot)
        g = gcd(e, tot)

    #HERE Use Extended Euclid's Algorithm (Included in RSA Library) to generate the private key
    
    #5PUBLIC KEY: (n,e) PRIVATE KEY: (d, n)
    return ((e, n), (d, n))
'''
dataInput = 'Advanced Security C14427818'
print (dataInput)

#Generating key
random = Random.new().read
key = RSA.generate(1024, random)

publicKey = key.publickey()
print "Public key =>" , publicKey

#Encrypting with key
encryptData = publicKey.encrypt(dataInput, 32)[0]
print (encryptData)

#Decrypting with key
decryptData = key.decrypt(encryptData)
print (decryptData)
