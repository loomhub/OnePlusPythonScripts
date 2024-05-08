from datetime import date
from pydantic import BaseModel, Field
from typing import List, Optional

class transactionTypeDTO(BaseModel):
    transaction_group : Optional[str] = None
    transaction_type : Optional[str] = None
    transaction_description : Optional[str] = None
    class Config:
        orm_mode = True
    
class transactionTypesListDTO(BaseModel):
    transactionTypes: List[transactionTypeDTO]
    class Config:
        orm_mode = True

TRANSACTION_TYPES_COLUMNS = {
    'Transaction Group': 'transaction_group',
    'Transaction Type': 'transaction_type',
    'Description': 'transaction_description'
}    