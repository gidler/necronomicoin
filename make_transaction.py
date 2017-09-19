#!/usr/bin/env python

import sys, os
import pickle as pkl
import codecs
import binascii

from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_PSS

from necromicoin import Transaction


def main(recipient, amount):
    # response = input('Send {} to {} [Yn]? '.format(amount, recipient))
    # if response.upper() != 'Y' and response.upper() != 'YES':
    #     print('Transaction cancelled.', file=sys.stderr)
        # return

    sender_private_key = RSA.importKey(open(os.path.expanduser('~/.nc/ncid_rsa')).read())
    sender_public_key = RSA.importKey(open(os.path.expanduser('~/.nc/ncid_rsa.pub')).read())
    recipient_public_key = RSA.importKey(open(recipient).read())
    signer = PKCS1_PSS.new(sender_private_key)
    transaction = Transaction(recipient_public_key, amount, sender_public_key)
    signature = signer.sign(transaction.compute_hash())
    # print(transaction.compute_hash().hexdigest(), file=sys.stderr)
    # print()
    # print(binascii.hexlify(signature), file=sys.stderr)
    # print()

    sys.stdout.buffer.write(pkl.dumps((transaction, binascii.hexlify(signature))))


if __name__ == '__main__':
    _, recipient, amount = sys.argv
    main(recipient, amount)
