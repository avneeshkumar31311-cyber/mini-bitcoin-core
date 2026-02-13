def mining_block(block,difficulty):
    prefix_str = '0'*difficulty        #Required Prefox for valid Hash.
    while True:
        block.hash = block.calculate_hash()
        if block.hash.startswith(prefix_str):
            return block
        else:
            block.nonce += 1        #Increase nonce and try again.