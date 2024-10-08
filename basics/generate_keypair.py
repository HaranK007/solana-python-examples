from solders.keypair import Keypair

key_pair = Keypair()
print("Generated Keypair : ", key_pair)
print("Public Key : " , key_pair.pubkey())

byte_array = key_pair.to_bytes_array()
print("Keypair in Byte array format : ", byte_array)

json = key_pair.to_json()
print("Keypair in JSON format : " , json)


# 67ZA4sxUBUU1x1k9ygkUiKoVJwwU1ZmNrKzXCK27NabKgBT2HbUFsRLfXpib4jyVfFLZYi29YnjkXHHkMQsfsYQD
# 5aLJg2WCyB6yp5TnTs8nbwsQjz3Z5TvHAMe2XmzgRRf3
