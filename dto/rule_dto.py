from datetime import date
from pydantic import BaseModel, Field
from typing import List, Optional

class ruleDTO(BaseModel):
    ttype : Optional[str] = None
    description : Optional[str] = None
    transaction_group : Optional[str] = None
    transaction_type : Optional[str] = None
    vendor : Optional[str] = None
    customer : Optional[str] = None
    vendor_no_w9 : Optional[str] = None
    customer_no_w9 : Optional[str] = None
    class Config:
        orm_mode = True
    
class rulesListDTO(BaseModel):
    rules: List[ruleDTO]
    class Config:
        orm_mode = True
        
RULES_COLUMNS = {
    'ttype': 'ttype',
    'description': 'description',
    'transaction_group': 'transaction_group',
    'transaction_type': 'transaction_type',
    'vendor': 'vendor',
    'customer': 'customer',
    'vendor_no_w9': 'vendor_no_w9',
    'customer_no_w9': 'customer_no_w9'
}

