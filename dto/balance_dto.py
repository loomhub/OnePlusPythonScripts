from datetime import date
from pydantic import BaseModel, Field
from typing import List, Optional

class balanceDTO(BaseModel):
    bank_account_key : Optional[str] = None
    snapshot : Optional[date] = None
    balance : Optional[float] = None
    class Config:
        json_encoders = {
            date: lambda v: v.strftime('%Y-%m-%d'),
            float: lambda v: float('nan') if v in [float('inf'), float('-inf'), float('nan')] else v
        }

class balancesListDTO(BaseModel):
    balances: List[balanceDTO]
    class Config:
        json_encoders = {
            date: lambda v: v.strftime('%Y-%m-%d'),
            float: lambda v: float('nan') if v in [float('inf'), float('-inf'), float('nan')] else v
        }
        orm_mode = True

BALANCES_COLUMNS = {
    'Property': 'bank_account_key',
    'Month': 'snapshot',
    'Balance': 'balance'  
}    