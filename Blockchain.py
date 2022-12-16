class Block:
  def __init__(self, data, previous_hash):
    self.data = data
    self.previous_hash = previous_hash
    self.hash = self.calc_hash()

  def calc_hash(self):
    sha = hashlib.sha256()
    hash_str = self.data.encode('utf-8')
    sha.update(hash_str)
    return sha.hexdigest()

class Blockchain:
  def __init__(self):
    self.chain = []

  def add_block(self, data):
    self.chain.append(Block(data, self.chain[-1].hash if len(self.chain) > 0 else None))

  def is_valid(self):
    for i in range(1, len(self.chain)):
      if self.chain[i].hash != self.chain[i].calc_hash():
        return False
      if self.chain[i].previous_hash != self.chain[i-1].hash:
        return False
    return True
