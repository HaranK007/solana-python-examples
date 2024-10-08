from solders.keypair import Keypair
# from mnemonic import Mnemonic

byte_array = [44, 99, 21, 123, 47, 89, 228, 27, 214, 190, 132, 201, 87, 38, 90, 112, 147, 34, 32, 44, 116, 6, 104, 95, 104, 190, 210, 146, 158, 106, 22, 183, 36, 119, 74, 188, 138, 240, 131, 120, 59, 145, 226, 16, 69, 230, 115, 175, 43, 168, 58, 215, 36, 72, 71, 67, 142, 153, 33, 215, 128, 213, 137, 251]

restored_from_byte_array = Keypair.from_bytes(byte_array)
print("Restored Keypair from Byte array : ", restored_from_byte_array)

base58_string = "tUM3Vj7mXyrXRLioRPJZ7rQ8n5nmToi27cw8ALefpNnwcshbhtnzzzEWf43ct9NataG7orVUyVCi4WXaMG7G1Fx"
restored_from_string = Keypair.from_base58_string(base58_string)
print("Restored Keypair from Base58 String : ", restored_from_string)


# mnemo = Mnemonic("english")
# seed = mnemo.to_seed("pill tomorrow foster begin walnut borrow virtual kick shift mutual shoe scatter")
# keypair = Keypair.from_seed(seed[:32])
