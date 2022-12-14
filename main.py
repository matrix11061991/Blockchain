# main.py file

"""

A simple Blockchain in Python

"""
class Block:

    def __init__(self, data, previous_hash):

        self.data = data

        self.previous_hash = previous_hash

        self.hash = self.calculate_hash()

        

    def calculate_hash(self):

        # Utiliser un algorithme de hachage pour calculer le hash du bloc

        pass

class Blockchain:

    def __init__(self):

        self.chain = [self.create_genesis_block()]

        

    def create_genesis_block(self):

        # Créer le premier bloc de la chaîne

        pass

    

    def get_previous_block(self):

        return self.chain[-1]

    

    def add_block(self, data):

        previous_block = self.get_previous_block()

        new_block = Block(data, previous_block.hash)

        self.chain.append(new_block)
