from datetime import date
from pydantic import BaseModel, Field
from typing import List, Optional

class partnerDTO(BaseModel):
    partner : Optional[str] = None
    recipient_type : Optional[str] = None
    recipient_tin_type : Optional[str] = None
    recipient_tin : Optional[str] = None
    last_name : Optional[str] = None
    first_name : Optional[str] = None
    address : Optional[str] = None
    city : Optional[str] = None
    state : Optional[str] = None
    zip_code : Optional[str] = None
    country : Optional[str] = None
    class Config:
        orm_mode = True
    
class partnersListDTO(BaseModel):
    partners: List[partnerDTO]
    class Config:
        orm_mode = True

PARTNERS_COLUMNS = {
    'Partner': 'partner',
    'Recipient Type': 'recipient_type',
    'Recipient TIN Type': 'recipient_tin_type',
    'Recipent TIN': 'recipient_tin',
    'R Business Name or Last Name': 'last_name',
    'R First Name': 'first_name',
    'R Address 1': 'address',
    'R City': 'city',
    'R State': 'state',
    'R Zip Code': 'zip_code',
    'R Country': 'country'
}