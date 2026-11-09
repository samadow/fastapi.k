from fastapi import APIRouter, HTTPException
from data.storage import book_list, author_list, categori_list, review_list
from schemas import book

router = APIRouter(prefix='/books', tags=['Books'])
book_id = 1


def check_author(author_id:int):
    for i in author_list:
        if i['id'] == author_id:
            return
    raise HTTPException(status_code=404, detail="Author not found")


def check_category(category_id:int):
    for i in categori_list:
        if i['id'] == category_id:
            return
    raise HTTPException(status_code=404, detail="Category not found")


@router.post("/creat_book", response_model=book.BookResponse)
async def creat_book(data:book.BookCreate):
    global book_id
    check_author(data.author_id)
    check_category(data.category_id)
    new_book = {
        "id":book_id,
        "title":data.title,
        "author_id":data.author_id,
        "category_id":data.category_id,
        "price":data.price,
        "published_year":data.published_year,
        "stock":data.stock,
        "description":data.description
    }
    book_id+=1
    book_list.append(new_book)
    return new_book


@router.get("/get_book")
async def get_book():
    return book_list


@router.get("/book_by_id/{book_id}")
async def book_by_id(book_id:int):
    for i in book_list:
        if i['id'] == book_id:
            return i
    raise HTTPException(status_code=404, detail="Book not found")


@router.put("/book_update/{book_id}", response_model=book.BookResponse)
async def update_book(book_id:int, data:book.BookCreate):
    for i in book_list:
        if i['id'] == book_id:
            check_author(data.author_id)
            check_category(data.category_id)
            i['title'] = data.title
            i['author_id'] = data.author_id
            i['category_id'] = data.category_id
            i['price'] = data.price
            i['published_year'] = data.published_year
            i['stock'] = data.stock
            i['description'] = data.description
            return i
    raise HTTPException(status_code=404, detail="Book not found")


@router.patch("/book_patch/{book_id}", response_model=book.BookResponse)
async def patch_book(book_id:int, data:book.BookUpdate):
    for i in book_list:
        if i['id'] == book_id:
            new_data = data.model_dump(exclude_unset=True)
            if 'author_id' in new_data:
                check_author(new_data['author_id'])
            if 'category_id' in new_data:
                check_category(new_data['category_id'])
            i.update(new_data)
            return i
    raise HTTPException(status_code=404, detail="Book not found")


@router.delete("/book_delete/{book_id}")
async def delete_book(book_id:int):
    for i in book_list:
        if i['id'] == book_id:
            book_list.remove(i)
            review_list[:] = [r for r in review_list if r['book_id'] != book_id]
            return {"message": "book udalit"}
    raise HTTPException(status_code=404, detail="Book not found")


@router.get("/{book_id}/reviews")
async def book_reviews(book_id:int):
    for i in book_list:
        if i['id'] == book_id:
            reviews = []
            for r in review_list:
                if r['book_id'] == book_id:
                    reviews.append(r)
            return reviews
    raise HTTPException(status_code=404, detail="Book not found")
