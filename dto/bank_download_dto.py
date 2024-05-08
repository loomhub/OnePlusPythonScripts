from datetime import date
from typing import List, Optional
from pydantic import BaseModel
import pandas as pd


class bankdownloadDTO(BaseModel):
    bank_account_key : Optional[str] = None
    tdate : Optional[date] = None
    description : Optional[str] = None
    amount : Optional[float] = None
    class Config:
        json_encoders = {
            date: lambda v: v.strftime('%Y-%m-%d') if v is not None else None,
            float: lambda v: v if isinstance(v, (int, float)) and not pd.isna(v) else None,
            pd.Timestamp: lambda v: v.strftime('%Y-%m-%d') if not pd.isna(v) else None
        }

class bankdownloadsListDTO(BaseModel):
    bankdownloads: List[bankdownloadDTO]
    
    class Config:
        json_encoders = {
            date: lambda v: v.strftime('%Y-%m-%d') if v is not None else None,
            float: lambda v: v if isinstance(v, (int, float)) and not pd.isna(v) else None,
            pd.Timestamp: lambda v: v.strftime('%Y-%m-%d') if not pd.isna(v) else None
        }

WELLSFARGO_FILEHEADERS = ['tdate','amount','not_required1','not_required2','description']
CHASE_FILEHEADERS = ['not_required1','tdate','description','amount','not_required2','not_required3','not_required4']

CHASE_COLUMNS = {
    'Details': 'not_required1',
    'Posting Date': 'tdate',
    'Description': 'description',
    'Amount': 'amount',
    'Type': 'not_required2',
    'Balance': 'not_required3',
    'Check or Slip #': 'not_required4'
}    
WELLSFARGO_COLUMNS = {
    'tdate': 'tdate',
    'amount': 'amount',
    'not_required1': 'not_required1',
    'not_required2': 'not_required2',
    'description': 'description'  
}    