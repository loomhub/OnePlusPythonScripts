from datetime import date
from pydantic import BaseModel, Field
from typing import List, Optional

class bankaccountDTO(BaseModel):
    bank_account_key : Optional[str] = None
    bank : Optional[str] = None
    account_type : Optional[str] = None
    account_number : Optional[str] = None
    llc : Optional[str] = None
    property_name : Optional[str] = None
    class Config:
        orm_mode = True
    
class bankaccountsListDTO(BaseModel):
    bankaccounts: List[bankaccountDTO]
    class Config:
        orm_mode = True

BANK_ACCOUNTS_COLUMNS = {
    'Bank Key': 'bank_account_key',
    'Bank': 'bank',
    'AccountType': 'account_type',
    'ExternalAccount': 'account_number',
    'LLC': 'llc',
    'Property': 'property_name'
}    