from typing import Optional
from pydantic import BaseModel


class ServiceInSchema(BaseModel):
    name: str
    description: Optional[str] = None
