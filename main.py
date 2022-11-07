# main.py file

"""

A simple Blockchain in Python

"""
import datetime
import json
import hashlib
from flask import Flask, jsonify
class Blockchain:
   def __init__(self):
       self.chain = []
       self.create_blockchain(proof=1, previous_hash='0')
   
  def create_blockchain(self, proof, previous_hash):
    block = {
      'index': len(self.chain) + 1,
      'timestamp': str(datetime.datetime.now()),
      'proof': proof,
      'previous_hash': previous_hash
    }
   self.chain.append(block)
   return block
  
  def get_previous_block(self):
    last_block = self.chain[-1]
    return last_block
  def proof_of_work(self, previous_proof):
    # miners proof submitted
    new_proof = 1
    # status of proof of work
    check_proof = False
    while check_proof is False:
       # problem and algorithm based off the previous proof and new proof
       hash_operation = hashlib.sha256(str(new_proof ** 2 - previous_proof ** 2).encode()).hexdigest()
       # check miners solution to problem, by using miners proof in cryptographic encryption
       # if miners proof results in 4 leading zero's in the hash operation, then:
       if hash_operation[:4] == '0000':
           check_proof = True
       else:
           # if miners solution is wrong, give mine another chance until correct
           new_proof += 1
    return new_proof
