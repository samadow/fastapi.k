from pydantic import BaseModel, Field


class ReviewCreate(BaseModel):
    book_id:int = Field(gt=0)
    reviewer_name:str = Field(min_length=2, max_length=80)
    rating:int = Field(ge=1, le=5)
    comment:str = Field(min_length=5, max_length=500)


class ReviewUpdate(BaseModel):
    book_id:int | None = Field(default=None, gt=0)
    reviewer_name:str | None = Field(default=None, min_length=2, max_length=80)
    rating:int | None = Field(default=None, ge=1, le=5)
    comment:str | None = Field(default=None, min_length=5, max_length=500)


class ReviewResponse(BaseModel):
    id:int
    book_id:int
    reviewer_name:str
    rating:int
    comment:str
