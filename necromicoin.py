#!/usr/bin/env python

from typing import Dict, Tuple, List

import hashlib
import time



def transaction(accounts: Dict[str, float],
                from_addr: str,
                to_addr: str,
                quantity: float) -> Dict[str, float]:
    ...


class Block:
    def __init__(self, block_num, transactions, timestamp, prev_block_hash):
        self._block_num = block_num
        self._transactions = transactions
        self._timestamp = timestamp
        self._prev_block_hash = prev_block_hash
        self._nonce = 0

    def compute_hash(self):
        return int(hashlib.sha256(str(sorted(self.__dict__.items())).encode('UTF-8')).hexdigest(), base=16)

    def mine(self):
        # print(self.compute_hash())
        # print(self.compute_hash() % 0xFFFF)
        # print('***')
        myhash = (self.compute_hash() % 0xFFFF)
        if 0x0FFF < myhash:
            print('you lose')
        else:
            print('you won with hash {}'.format(hex(myhash)))
            return myhash
        self._nonce += 1

def main():
    blk = Block(0, [], int(time.time()), 'asdasdasdasads')
    # ahash = int(blk.compute_hash().hexdigest(), base=16)
    # print()
    winning_hash = None
    while not winning_hash:
        winning_hash = blk.mine()
        # blk.mine()

if __name__ == '__main__':
    main()