from solders.pubkey import Pubkey

def find_inscription_shard_pda(shard_number : int, program_id : Pubkey) -> Pubkey:
    
    seeds = [
        b'Inscription',
        b'Shard',
        bytes(program_id),
        bytes([shard_number])
    ]
    
    pda , bump = Pubkey.find_program_address(seeds,program_id)
    return pda