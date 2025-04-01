from pydantic import BaseModel, Field


class Item(BaseModel):
    name: str = Field(example="Тостер", min_length=2 ,max_length=100)
    price: float = Field(example="100", gt=0)
    description : str | None =Field(example="Тостер жарит классно", max_length=500)

