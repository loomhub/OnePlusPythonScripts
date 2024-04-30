from typing import List, Optional

from pydantic import BaseModel


class processedDTO(BaseModel):
    report : Optional[str] = None
    receiver : Optional[str] = None

class listProcessedDTO(BaseModel):
    done: List[processedDTO] = []