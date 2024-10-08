import asyncio
from os import error
from solana.rpc.async_api import AsyncClient
from solders.pubkey import Pubkey

pubkey = Pubkey.from_string("5aLJg2WCyB6yp5TnTs8nbwsQjz3Z5TvHAMe2XmzgRRf3")

async def main():
    async with AsyncClient("https://api.devnet.solana.com") as Client :
        
        if await Client.is_connected() :
            # request_airdrop method parameters [Public Key, Lamports, Commitment(Optional)]
            try:
                airdrop = await Client.request_airdrop(pubkey,1000000000)
                print(airdrop)
            except(error):
                print("Error Occured during airdrop, ",error)
        else:
            print("Client is not connected")

asyncio.run(main())