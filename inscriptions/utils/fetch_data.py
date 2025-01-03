from solders.pubkey import Pubkey
from solana.rpc.async_api import AsyncClient

async def fetch_data(client : AsyncClient, pub_key : Pubkey):
    try:
        res = await client.get_account_info(pubkey=pub_key)
        if res.value:
            print(res.value)
        else:
            print("No data found")
    except Exception as e:
        print("Error occured : ",e)

