from pydantic import BaseModel

class FormData(BaseModel):
    name: str
    email: str
    message: str
