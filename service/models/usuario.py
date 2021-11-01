from pydantic import BaseModel


class Usuario(BaseModel):
    id: int
    email: str
    senha: str
