## Overview

This project is a simplified simulation of the Bitcoin protocol implemented in Python.  
It demonstrates how blocks are linked using hashes, how Merkle Trees ensure transaction integrity, and how a basic Proof-of-Work mining works.

The purpose is to learn blockchain security, data integrity, and protocol-level systems. This project is mainly for educational purposes and portfolio demonstration for **Summer of Bitcoin 2026** application.

---

## Features

**Block Creation and Hashing** – Each block has an index, timestamp, previous hash, and nonce. Transactions are simplified.

**Merkle Tree Construction** – Demonstrates how transactions can be summarized and verified in a block  

**Proof-of-Work Mining Simulation** – Demonstrates simplified mining and block validation  

**Blockchain Validation** – Checks that blocks are linked correctly and hashes are consistent

## Project Structure


mini-bitcoin-core/
 ├── src/                 # All Python source code
 │    ├── block.py        # Block class + hashing
 │    ├── merkle.py       # Merkle tree logic
 │    ├── mining.py       # Proof-of-Work mining
 │    └── blockchain.py   # Blockchain logic + validation
 ├── main.py              # Entry point / demo runs
 ├── README.md            # Project description + design
 └── requirements.txt     # Python dependencies (probably empty)


## Getting Started


Clone the repository
Install Python 3.10 , if not installed.
Run the demo.



##Learning Takeaways
Understand **block structure and hash chaining**
Learn how **Merkle Trees** summarize transactions
See how **Proof-of-Work** mining works in a simplified simulation
Understand **basic blockchain immutability**
