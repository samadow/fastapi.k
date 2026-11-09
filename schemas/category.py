from fastapi import FastAPI,Query, Path,HTTPException
from pydantic import BaseModel, Field, EmailStr
from data.storage import categori_list
from fastapi import APIRouter
router = APIRouter(prefix='/categories', tags=['Categories'])

class CategoryCreate(BaseModel):
    name:str = Field(min_length=3,max_length=100)
    description:str = Field(min_length=3,max_length=100)
  
  
class CategoryUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=3, max_length=100)
    description: str | None = Field(default=None, min_length=2, max_length=60)

  
class CategoryResponse(BaseModel):
    id:int
    name:str = Field(min_length=3,max_length=100)
    description:str = Field(min_length=3,max_length=100)
        
    
    
    
