from datetime import date
from pydantic import BaseModel, Field


class BookCreate(BaseModel):
    title:str = Field(min_length=2, max_length=150)
    author_id:int = Field(gt=0)
    category_id:int = Field(gt=0)
    price:float = Field(gt=0)
    published_year:int = Field(ge=1450, le=date.today().year)
    stock:int = Field(ge=0)
    description:str | None = Field(default=None, max_length=1000)


class BookUpdate(BaseModel):
    title:str | None = Field(default=None, min_length=2, max_length=150)
    author_id:int | None = Field(default=None, gt=0)
    category_id:int | None = Field(default=None, gt=0)
    price:float | None = Field(default=None, gt=0)
    published_year:int | None = Field(default=None, ge=1450, le=date.today().year)
    stock:int | None = Field(default=None, ge=0)
    description:str | None = Field(default=None, max_length=1000)


class BookResponse(BaseModel):
    id:int
    title:str
    author_id:int
    category_id:int
    price:float
    published_year:int
    stock:int
    description:str | None = None
