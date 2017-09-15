#!/usr/bin/env python

from Crypto.PublicKey import RSA
from Crypto import Random

key = RSA.generate(2048)

with open( 'ncid_rsa', 'wb') as priv_fo:
    priv_fo.write(key.exportKey('PEM'))

with open( 'ncid_rsa.pub', 'wb') as pub_fo:
    pub_fo.write(key.publickey().exportKey('PEM'))
