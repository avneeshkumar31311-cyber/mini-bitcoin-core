from src.block import Block
from src.mining import mining_block

class BlockChain:

    def __init__(self, difficulty=3):
        self.chain = []
        self.difficulty = difficulty
        self.create_genesis_block()

    def create_genesis_block(self):  # Creation of the first block
        genesis_block = Block(0, "Genesis Block", "0")
        self.chain.append(genesis_block)

    def get_latest_block(self):   #link the blocks
        return self.chain[-1]

    def add_block(self, new_block):     #add new blocks
        new_block.prev_hash = self.get_latest_block().hash
        mining_block(new_block, self.difficulty)
        self.chain.append(new_block)

    def is_chain_valid(self):        #check the blockcian isn't tampered 
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != current_block.calculate_hash():
                return False

            if current_block.prev_hash != previous_block.hash:
                return False

        return True

    def print_chain(self):
        for block in self.chain:
            print("-" * 60)
            print(f"Index: {block.idx}")
            print(f"Timestamp: {block.timestamp}")
            print(f"Data: {block.data}")
            print(f"Previous Hash: {block.prev_hash}")
            print(f"Hash: {block.hash}")
            print(f"Nonce: {block.nonce}")
