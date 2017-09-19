#!/usr/bin/env python

import sys, os
import pickle as pkl

from necromicoin import Transaction, Blockchain


def main(transaction):
    transaction, signature = pkl.loads(open(transaction, 'rb').read())
    print(transaction.compute_hash().hexdigest(), file=sys.stderr)
    print(signature, file=sys.stderr)
    # import ipdb; ipdb.set_trace()
    if not transaction.verify(signature):
        print('invalid transaction!', file=sys.stderr)
        exit(1)


if __name__ == '__main__':
    _, transaction = sys.argv
    main(transaction)
