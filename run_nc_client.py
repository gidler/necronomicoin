#!/usr/bin/env python

import sys

from necronomicoin import Block, Transaction, get_current_hash_difficulty

def run_nc_client(miner_public_key):

    current_block = Block(0, [], int(time.time()), 'asdasdasdasads')
    hash_limit = get_current_hash_difficulty(current_block._block_num)

    while True:

        # interupt by another client finding a block
        # 

        myhash = current_block.compute_hash()
        if myhash < hash_limit:
            print('you won with hash {}'.format(hex(myhash)))
            break
        else:
            print('you lose')
            self._nonce += 1

if __name__ == '__main__':
    if len(sys.argv) == 2:
        miner_pub_key = sys.argv[1] 
    else:
        miner_public_key = RSA.importKey(open(os.path.expanduser('~/.nc/ncid_rsa.pub')).read())
    run_nc_client(miner_public_key)
