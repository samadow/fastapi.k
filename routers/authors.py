from fastapi import APIRouter, HTTPException,Path,Query
from schemas import author
from data.storage import author_list, book_list

router = APIRouter(prefix='/authors', tags=['Authors'])
next_id = 2

@router.post("/creat_author",response_model=author.AuthorResponse)
async def creat_author(data:author.AuthorCreate):
    global next_id
    new_author = {
        "id":next_id,
        "name":data.name,
        "country":data.country,
        "birth_year":data.birth_year
    }
    next_id+=1
    author_list.append(new_author)
    return new_author

@router.get("/get_author")
async def author_get():
    return author_list


@router.get("/get_author_id/{author_id}")
async def get_by_id(author_id:int):
    for i in author_list:
        if i['id'] == author_id:
            return i
    raise HTTPException(status_code=404, detail="Author not found")


@router.delete("/delet_author/{author_id}")
async def delet_author(author_id:int):
    for i in author_list:
        if i["id"] == author_id:
            author_list.remove(i)
            return {"message": "author udalit"}
    raise HTTPException(status_code=404, detail="Author not found")


@router.patch("/patch_author/{author_id}", response_model=author.AuthorResponse)
async def patch_author(author_id: int, data: author.AuthorPatch):
    for i in author_list:
        if i["id"] == author_id:
            new_data = data.model_dump(exclude_unset=True)
            i.update(new_data)
            return i
    raise HTTPException(status_code=404, detail="Author not found")


@router.get("/{author_id}/books")
async def author_books(author_id:int):
    for i in author_list:
        if i['id'] == author_id:
            books = []
            for b in book_list:
                if b['author_id'] == author_id:
                    books.append(b)
            return books
    raise HTTPException(status_code=404, detail="Author not found")
