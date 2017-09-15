#!/usr/bin/env python

import sys, os, codecs

from Crypto.Signature import PKCS1_PSS
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto import Random

def output(*args):
    for s in args:
        if type(s) is str:
            s = s.encode('ascii')
        sys.stdout.buffer.write(codecs.encode(s, 'hex'))
    sys.stdout.buffer.flush()

def main(recipient, amount):
    private_key = RSA.importKey(open(os.path.expanduser('~/.nc/ncid_rsa')).read())
    public_key = RSA.importKey(open(os.path.expanduser('~/.nc/ncid_rsa.pub')).read())
    h = SHA.new()
    h.update(recipient.encode('UTF-8'))
    h.update(str(amount).encode('UTF-8'))
    signer = PKCS1_PSS.new(private_key)
    signature = signer.sign(h)

    output(recipient, '----', amount, '----', public_key.exportKey('DER'), '----', signature)#, ' ', amount, public_key.exportKey('DER'))
    sys.stdout.write('\n')


if __name__ == '__main__':
    _, recipient, amount = sys.argv
    main(recipient, amount)
