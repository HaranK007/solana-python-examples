from solders.pubkey import Pubkey
from solders.instruction import AccountMeta, Instruction # type: ignore
from solders.system_program import ID as SYSTEM_PROGRAM

def initialize(program_id: Pubkey, payer : Pubkey, inscription_account : Pubkey, inscription_metadata_account : Pubkey,inscription_shared_account : Pubkey) -> Instruction:
    accounts = [
        AccountMeta(inscription_account,is_signer=True,is_writable=True),
        AccountMeta(inscription_metadata_account,is_signer=False,is_writable=True),
        AccountMeta(inscription_shared_account,is_signer=False,is_writable=True),
        AccountMeta(payer,is_signer=True,is_writable=True), 
        AccountMeta(inscription_account,is_signer=True,is_writable=False),
        AccountMeta(SYSTEM_PROGRAM,is_signer=False,is_writable=False),
    ]
    
    instruction_data = bytes([0])
    
    return Instruction(program_id=program_id,data=instruction_data,accounts=accounts)