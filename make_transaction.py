#!/usr/bin/env python

import sys, os

from Crypto.Signature import PKCS1_PSS
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto import Random


def main(recipient, amount):
    private_key = RSA.importKey(open(os.path.expanduser('~/.nc/ncid_rsa')).read())
    public_key = RSA.importKey(open(os.path.expanduser('~/.nc/ncid_rsa.pub')).read())
    h = SHA.new()
    h.update(recipient.encode('UTF-8'))
    h.update(str(amount).encode('UTF-8'))
    signer = PKCS1_PSS.new(private_key)
    signature = signer.sign(h)
    # import ipdb; ipdb.set_trace()
    # sys.stdout.write()
    # sys.stdout.write(hex(' '))
    # sys.stdout.buffer.write(' '.encode('UTF-8'))
    print(recipient + amount + public_key.exportKey('DER') + signature)

if __name__ == '__main__':
    _, recipient, amount = sys.argv
    main(recipient, amount)
