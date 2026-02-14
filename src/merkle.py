import hashlib

def sha256(data):
    return hashlib.sha256(data.encode()).hexdigest()

def merkle_root(txs):
    if not txs:
        return None
    
    level = [sha256(tx) for tx in txs]

    while len(level) > 1:
        if len(level) % 2 == 1:
            level.append(level[-1])  # Duplicate last hash if odd.
        
        #Combine pairs of hashes and hash them again.
        level = [sha256(level[i] + level[i + 1]) for i in range(0, len(level), 2)]

    return level[0]     #Final remaining hash is the Merkle Root.