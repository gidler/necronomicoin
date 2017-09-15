#!/usr/bin/env python

import sys

from Crypto.Signature import PKCS1_PSS
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto import Random


def main(recipient, amount):
    private_key = RSA.importKey(open('~/.nc/ncid_rsa').read())
    public_key = RSA.importKey(open('~/.nc/ncid_rsa.pub').read())
    h = SHA.new()
    h.update(recipient)
    h.update(str(amount).encode('ascii'))
    signer = PKCS1_PSS.new(private_key)
    signature = signer.sign(h)
    print(f'{recipient} {amount} {public_key} {signature}')

if __name__ == '__main__':
    recipient, amount = sys.argv
    main(recipient, float(amount))
