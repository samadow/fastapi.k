from fastapi import FastAPI,Query, Path,HTTPException
from pydantic import BaseModel, Field, EmailStr
from data.storage import author_list
from fastapi import APIRouter
router = APIRouter(prefix='/authors', tags=['Authors'])




class AuthorCreate(BaseModel):
    name: str = Field(min_length=3, max_length=100)
    country:str = Field(min_length=2, max_length=60)
    birth_year:int
    
    


class AuthorPatch(BaseModel):
    name: str | None = Field(default=None, min_length=3, max_length=100)
    country: str | None = Field(default=None, min_length=2, max_length=60)
    birth_year: int | None = None

    


class AuthorResponse(BaseModel):
    id: int
    name: str = Field(min_length=3, max_length=100)
    country:str = Field(min_length=2, max_length=60)
    birth_year:int
    
    
