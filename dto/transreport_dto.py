from datetime import date
from pydantic import BaseModel, Field
from typing import List, Optional

class transreportDTO(BaseModel):
    sequence_id : Optional[int] = None
    category : Optional[str] = None
    calc_method : Optional[str] = None
    fields : Optional[str] = None
    class Config:
        orm_mode = True
    
class transreportsListDTO(BaseModel):
    transreports: List[transreportDTO]
    class Config:
        orm_mode = True
        
TRANSREPORTS_COLUMNS = {
    'sequence_id': 'sequence_id',
    'category': 'category',
    'calc_method': 'calc_method',
    'fields': 'fields'
}

