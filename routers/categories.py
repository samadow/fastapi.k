from fastapi import FastAPI,Query, Path,HTTPException
from pydantic import BaseModel, Field, EmailStr
from data.storage import categori_list, book_list
from fastapi import APIRouter
from schemas import category
router = APIRouter(prefix='/categories', tags=['Categories'])
cate_id = 2

@router.post("/creatcategori", response_model=category.CategoryResponse)
async def creat_categori(data:category.CategoryCreate):
    global cate_id
    new_category = {
        "id":cate_id,
        "name":data.name,
        "description":data.description
    }
    cate_id+=1
    categori_list.append(new_category)
    return new_category

@router.get("/get_category")
async def ge_category():
    return categori_list

@router.get("/category_by_id/{category_id}")
async def getby_id(category_id:int):
    for i in categori_list:
        if i['id'] == category_id:
            return i
    raise HTTPException(status_code=404, detail="Category not found")


@router.delete("/category_delte_id/{category_id}")
async def getby_id_delete(category_id:int):
    for i in categori_list:
        if i['id'] == category_id:
            categori_list.remove(i)
            return categori_list
    raise HTTPException(status_code=404, detail="Category not found")


@router.put("/category_update/{category_id}", response_model=category.CategoryResponse)
async def update_category(category_id:int, data:category.CategoryCreate):
    for i in categori_list:
        if i['id'] == category_id:
            i['name'] = data.name
            i['description'] = data.description
            return i
    raise HTTPException(status_code=404, detail="Category not found")


@router.patch("/category_patch/{category_id}", response_model=category.CategoryResponse)
async def patch_category(category_id:int, data:category.CategoryUpdate):
    for i in categori_list:
        if i['id'] == category_id:
            new_data = data.model_dump(exclude_unset=True)
            i.update(new_data)
            return i
    raise HTTPException(status_code=404, detail="Category not found")


@router.get("/{category_id}/books")
async def category_books(category_id:int):
    for i in categori_list:
        if i['id'] == category_id:
            books = []
            for b in book_list:
                if b['category_id'] == category_id:
                    books.append(b)
            return books
    raise HTTPException(status_code=404, detail="Category not found")
