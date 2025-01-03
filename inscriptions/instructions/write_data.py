from solders.pubkey import Pubkey
from solders.instruction import Instruction, AccountMeta
from solders.system_program import ID as SYSTEM_PROGRAM

def write_data(program_id : Pubkey,
               inscription_account : Pubkey, 
               inscription_metadata_account : Pubkey, 
               payer : Pubkey, 
               write_data : bytes) -> Instruction:
    
    accounts = [
        AccountMeta(pubkey = inscription_account, is_signer= False, is_writable = True),
        AccountMeta(pubkey = inscription_metadata_account, is_signer= False, is_writable = True),
        AccountMeta(pubkey = payer, is_signer= True, is_writable = True),
        AccountMeta(pubkey = inscription_account, is_signer= True, is_writable = True),
        AccountMeta(pubkey = SYSTEM_PROGRAM, is_signer= False, is_writable = True),
    ]
    
    instruction_data = bytes([3]) + write_data
    
    return Instruction(program_id=program_id,
                       data=instruction_data,
                       accounts=accounts)