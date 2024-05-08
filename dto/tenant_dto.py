from datetime import date
from pydantic import BaseModel, Field
from typing import List, Optional

class tenantDTO(BaseModel):
    customer : Optional[str] = None
    property_name : Optional[str] = None
    unit_name : Optional[str] = None
    lease_start : Optional[date] = None
    lease_end : Optional[date] = None
    rent : Optional[float] = None
    security_deposit : Optional[float] = None
    class Config:
        orm_mode = True
    
class tenantsListDTO(BaseModel):
    tenants: List[tenantDTO]
    class Config:
        orm_mode = True
        
TENANTS_COLUMNS = {
    'Tenant': 'customer',
    'Property': 'property_name',
    'Unit': 'unit_name',
    'Lease Start': 'lease_start',
    'Lease End': 'lease_end',
    'Rent': 'rent',
    'Security Deposit': 'security_deposit'
}    