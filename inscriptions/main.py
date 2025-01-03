import asyncio
from solana.rpc.async_api import AsyncClient
from instructions import initialize,write_data
from solders.pubkey import Pubkey
from solders.keypair import Keypair # type: ignore
from constants import INSCRIPTION_PROGRAM_ID
from utils.find_metadata_pda import find_inscription_metadata_pda
from utils.find_shard_pda import find_inscription_shard_pda
from utils.serialize_data import serialize_write_data_instruction
from utils.fetch_data import fetch_data
from solana.transaction import Transaction

async def main():
    
    async with AsyncClient("https://api.devnet.solana.com") as client:
        inscription_acc = Keypair.from_base58_string("3UfTNvSKETtjnoaUE6LCHnGwaHz5jDnRJy8LV6acEbaTrrTjss99RZdSbxkcqCPm8tKawPyXBsiR2aUA46MNbHtj")
        print("Keypair : ",inscription_acc)
        program_id = Pubkey.from_string(INSCRIPTION_PROGRAM_ID)
        
        payer = Keypair.from_base58_string("tUM3Vj7mXyrXRLioRPJZ7rQ8n5nmToi27cw8ALefpNnwcshbhtnzzzEWf43ct9NataG7orVUyVCi4WXaMG7G1Fx")
        inscription_metadata_account = find_inscription_metadata_pda(inscription_account=inscription_acc.pubkey(),program_id=program_id)
        inscription_shared_account = find_inscription_shard_pda(shard_number=0,program_id=program_id)
        print("Metadata Account PDA : ",inscription_metadata_account)
        print("Shard Account PDA : ",inscription_shared_account)
        
        associated_tag = "SomeTag"  
        offset = 42  
        value = b'{"description": "A bread! But onchain!", "external_url": "https://breadheads.io"}'

        data = serialize_write_data_instruction(associated_tag=None,offset=1,value=[124,8,9])
        

        # tx_instruction = initialize.initialize(program_id=program_id, payer=payer.pubkey() ,inscription_account=inscription_acc.pubkey(),inscription_metadata_account=inscription_metadata_account,inscription_shared_account=inscription_shared_account)
        tx_instruction = write_data.write_data(program_id=program_id,inscription_account=inscription_acc.pubkey(),inscription_metadata_account=inscription_metadata_account,payer=payer.pubkey(),write_data=data)
        
        tx = Transaction().add(tx_instruction)
        try:
            recent_blockhash_resp = await client.get_latest_blockhash()
            print("Latest blockhash : ",recent_blockhash_resp.value.blockhash)
            recent_blockhash = recent_blockhash_resp.value.blockhash

            tx.recent_blockhash = recent_blockhash
            tx.fee_payer = payer.pubkey()
            res = await client.send_transaction(tx,payer,inscription_acc)
            print(res)
            await fetch_data(client=client,pub_key=inscription_acc.pubkey())
        except Exception as error:
            print("Error Occured", error)
        
        # await fetch_data(client=client,pub_key=inscription_acc.pubkey())
            
asyncio.run(main())