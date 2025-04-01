from pydantic import BaseModel, Field


class Item(BaseModel):
    name:str = Field(example="Ноутбук", max_length=20)
    description : str | None = None
    price: float
    tax: float | None = None
