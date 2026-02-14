# This File is Basically for testing and Output of Project.


from src.blockchain import BlockChain
from src.block import Block
from src.merkle import merkle_root


def test_merkle():
    print("\n--- Testing Merkle Tree ---")
    txs = ["tx1", "tx2", "tx3", "tx4"]
    root = merkle_root(txs)
    print("Transactions:", txs)
    print("Merkle Root:", root)


def test_blockchain():
    print("\n--- Testing Blockchain Mining ---")

    bc = BlockChain(difficulty=3) #Creating a blockchain of difficulty 3.

    print("Mining block 1...")
    block1 = Block(1, "First transaction", bc.get_latest_block().hash)
    bc.add_block(block1)

    print("Mining block 2...")
    block2 = Block(2, "Second transaction", bc.get_latest_block().hash)
    bc.add_block(block2)

    print("\n--- Blockchain ---")
    bc.print_chain() # Display the blockchain.


def main():
    test_merkle()  # run the merkle tree test.
    test_blockchain() #Whether the blockchain is working properly or not.


if __name__ == "__main__":
    main()
