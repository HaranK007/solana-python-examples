from solana.rpc.api import Client
from solders.pubkey import Pubkey

solana_client = Client("https://api.devnet.solana.com")

account_info = solana_client.get_account_info(Pubkey.from_string("3TMBQtc3DVkKvMxgP2emyxtfFBPVe6XhXMVRbjLwVHGv"))

if account_info.value:
    lamports = account_info.value.lamports
    owner = account_info.value.owner
    executable = account_info.value.executable
    print("lamports : ", lamports)
    print("owner : ", owner)
    print("executable : ", executable)
else:
    print("Account data not Found")
    
