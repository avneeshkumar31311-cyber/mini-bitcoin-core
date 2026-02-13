from src.blockchain import BlockChain
from src.block import Block

bc = BlockChain(difficulty=3)

print("Mining block 1...")
block1 = Block(1, "First transaction", bc.get_latest_block().hash)
bc.add_block(block1)

print("Mining block 2...")
block2 = Block(2, "Second transaction", bc.get_latest_block().hash)
bc.add_block(block2)

bc.print_chain()
