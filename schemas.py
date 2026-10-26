from pydantic import BaseModel

class ProductCreate(BaseModel):
    name: str
    description: str | None = None
    price: float

class ProductResponse(BaseModel):
    id: int
    name: str
    description: str | None = None
    price: float

    class Config:
        from_attributes = True  # was orm_mode = True in older Pydantic
