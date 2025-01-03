from borsh_construct import U64, U8, Option,Vec,String,CStruct
from typing import Optional,List

def serialize_write_data_instruction(
    associated_tag: Optional[str],  # Optional string
    offset: int,                    # u64
    value: List[int]                    # Byte array
) -> bytes:
    
    write_data_args = CStruct(
        "associated_tag" / Option(String),
        "offset" / U64,
        "value" / Vec(U8) 
    )
    
    data = {
        "associated_tag" : associated_tag if associated_tag else None,
        "offset" : offset,
        "value" : value
    }
    
    serialized_data = write_data_args.build(data)
    
    return serialized_data
