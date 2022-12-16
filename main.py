class Block:
  def __init__(self, index, timestamp, data, previous_hash):
    self.index = index
    self.timestamp = timestamp
    self.data = data
    self.previous_hash = previous_hash
    self.hash = self.calc_hash()
  
  def calc_hash(self):
    sha = hashlib.sha256()
    hash_str = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}"
    sha.update(hash_str.encode('utf-8'))
    return sha.hexdigest()

class Blockchain:
  def __init__(self):
    self.chain = [self.create_genesis_block()]
  
  def create_genesis_block(self):
    return Block(0, datetime.datetime.now(), "Genesis Block", "0")
  
  def get_last_block(self):
    return self.chain[-1]
  
  def add_block(self, new_block):
    new_block.previous_hash = self.get_last_block().hash
    new_block.hash = new_block.calc_hash()
    self.chain.append(new_block)

blockchain = Blockchain()

blockchain.add_block(Block(1, datetime.datetime.now(), "Some data here", "0"))
blockchain.add_block(Block(2, datetime.datetime.now(), "More data here", "0"))
blockchain.add_block(Block(3, datetime.datetime.now(), "Even more data here", "0"))

print(blockchain.chain)
