from datetime import date
from pydantic import BaseModel, Field
from typing import List, Optional
import pandas as pd

class propertyMasterDTO(BaseModel):
    property_name : Optional[str] = 'General'
    property_description : Optional[str] = 'General'
    llc : Optional[str] = 'LLC'
    note : Optional[str] = 'LLC'
    purchase_date : Optional[date] = date(1900,1,1)
    sell_date : Optional[date] = date(1900,1,1)
    purchase_price : Optional[float] = 0
    sell_price : Optional[float] = 0
    units: Optional[int] = 0
    county: Optional[str] = 'General'
    class Config:
        json_encoders = {
            date: lambda v: v.strftime('%Y-%m-%d') if v is not None else None,
            float: lambda v: v if isinstance(v, (int, float)) and not pd.isna(v) else None,
            pd.Timestamp: lambda v: v.strftime('%Y-%m-%d') if not pd.isna(v) else None
        }
        orm_mode = True

class propertyMastersListDTO(BaseModel):
    propertyMasters: List[propertyMasterDTO]
    class Config:
        orm_mode = True
        
PROPERTY_MASTER_COLUMNS = {
    'Property': 'property_name',
    'Property Description': 'property_description',
    'LLC': 'llc',
    'Title': 'note',
    'Purchase Date': 'purchase_date',
    'Sell Date': 'sell_date',
    'Purchase Price': 'purchase_price',
    'Sell Price': 'sell_price',
    'Units': 'units',
    'County': 'county'
}
    