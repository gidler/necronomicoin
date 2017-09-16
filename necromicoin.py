#!/usr/bin/env python

from typing import Dict, Tuple, List
import hashlib
import time

class Transaction:
    def __init__(self, recipient_key, amount, sender_key):
        self._recipient_key = recipient_key
        self._amount = amount
        self._sender_key = sender_key

class Block:
    def __init__(self, block_num, transactions, timestamp, prev_block_hash):
        self._block_num = block_num
        self._transactions = transactions
        self._timestamp = timestamp
        self._prev_block_hash = prev_block_hash
        self._nonce = 0

    def compute_hash(self):
        return int(hashlib.sha256(str(sorted(self.__dict__.items())).encode('UTF-8')).hexdigest(), base=16)

class Blockchain:
    def __init__():
        genesis_block = Block(0, [], int(time.time()), '0000000000000000000000000000000')
        self._blocks = [genesis_block]
        self._balances = {}

    def get_current_hash_difficulty():
        # get number of last block on chain and calculate
        # hash difficulty as a function of it
        return 0x0FFF

    def add_block_to_chain(self, block):
        self._blocks.append(block)

    def verify_sender(self, sender_public_key, amount):
        if sender_public_key in self._balances and self._balances[sender_public_key] >= amount:
            return True
        else:
            return False

    def verify_recipient(self, recipient_public_key):
        return True

    def verify_amount(amount):
        return amount > 0

    def verify_timestamp(self, timestamp)
        return self._blocks[-1].timestamp < timestamp < int(time.time())

    def verify_transaction(self, transaction):
        valid = self.verify_amount and self.verify_sender and self.verify_recipient and self.verify_timestamp
        return valid

    def verify_block(self, block):
        # check all the fields in a candidate block
        if block._block_num != self._blocks[-1]._block_num + 1
            print("Candidate block FAILED due to invalid: block_num")
            return False
        for transaction in block._transactions:
            if not verify_transaction(transaction):
                print("Candidate block FAILED due to invalid: bad transaction")
                return False
        if not verify_timestamp(block._timestamp):
                print("Candidate block FAILED due to invalid: time_stamp")
                return False
        if block._prev_block_hash != self._blocks[-1].compute_hash()
            print("Candidate block FAILED due to invalid: prev_block_hash")
            return False
        # finally, if all else works, check hash
        hash_limit = 
        if block.compute_hash() < this.get_current_hash_difficulty():
            print("Candidate block FAILED due to invalid: hash_difficulty")
            return False
        # Block is valid
        return True
