from solders.pubkey import Pubkey

def find_inscription_metadata_pda(inscription_account: Pubkey, program_id: Pubkey) -> Pubkey:
    
    seeds = [
        b'Inscription',                       # Seed 1: String
        bytes(program_id),                    # Seed 2: Serialized Program ID
        bytes(inscription_account)            # Seed 3: Serialized Inscription Account public key
    ]
    
    pda, bump = Pubkey.find_program_address(seeds, program_id)
    return pda
