import asyncio
from solana.rpc.async_api import AsyncClient
from solders.keypair import Keypair
from solders.system_program import transfer, TransferParams
from solana.transaction import Transaction

key_pair = Keypair.from_base58_string("tUM3Vj7mXyrXRLioRPJZ7rQ8n5nmToi27cw8ALefpNnwcshbhtnzzzEWf43ct9NataG7orVUyVCi4WXaMG7G1Fx")
sender, receiver = key_pair.pubkey(), Keypair().pubkey() 
instruction = transfer(TransferParams(from_pubkey=sender, to_pubkey=receiver, lamports=10000000))
print(key_pair.pubkey())
tx = Transaction().add(instruction).add(instruction)

async def main():
    async with AsyncClient("https://api.devnet.solana.com") as client:  
        if await client.is_connected():
            try:
                res = await client.send_transaction(tx, key_pair)
                print(f"Transaction result: {res}")
            except Exception as e:
                print(f"Error sending transaction: {e}")
        else:
            print("Client not connected")

asyncio.run(main())
