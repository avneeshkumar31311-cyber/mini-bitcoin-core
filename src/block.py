import hashlib
import time

class Block:

    def __init__(self,idx,data,prev_hash):
        self.idx = idx                          #Block Number
        self.timestamp = time.time()            #time of Block Creation
        self.data = data                        #Block's Data
        self.prev_hash = prev_hash              # Hash pf previous Block
        self.nonce = 0                          # Counter used for mining
        self.hash = self.calculate_hash()

    def calculate_hash(self):
            #Convert all block fields into one string
            text = f"{self.idx}{self.timestamp}{self.data}{self.prev_hash}{self.nonce}"

            #Calculate SHA-256 hash
            return hashlib.sha256(text.encode()).hexdigest()