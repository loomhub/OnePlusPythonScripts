from datetime import date
from pydantic import BaseModel, Field
from typing import List, Optional

class llcDTO(BaseModel):
    llc : Optional[str] = None
    ein : Optional[str] = None
    llc_address : Optional[str] = None
    llc_description : Optional[str] = None
    formation_date : Optional[date] = None
    class Config:
        orm_mode = True  

class llcsListDTO(BaseModel):
    llcs: List[llcDTO]
    class Config:
        orm_mode = True

LLC_COLUMNS = {
    'llc': 'llc',
    'ein': 'ein',
    'llc_adddress': 'llc_address',
    'llc_description': 'llc_description',
    'formation_date': 'formation_date'
}    