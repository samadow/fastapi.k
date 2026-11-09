from fastapi import APIRouter, HTTPException
from data.storage import review_list, book_list
from schemas import review

router = APIRouter(prefix='/reviews', tags=['Reviews'])
review_id = 1


def check_book(book_id:int):
    for i in book_list:
        if i['id'] == book_id:
            return
    raise HTTPException(status_code=404, detail="Book not found")


@router.post("/creat_review", response_model=review.ReviewResponse)
async def creat_review(data:review.ReviewCreate):
    global review_id
    check_book(data.book_id)
    new_review = {
        "id":review_id,
        "book_id":data.book_id,
        "reviewer_name":data.reviewer_name,
        "rating":data.rating,
        "comment":data.comment
    }
    review_id+=1
    review_list.append(new_review)
    return new_review


@router.get("/get_review")
async def get_review():
    return review_list


@router.get("/review_by_id/{review_id}")
async def review_by_id(review_id:int):
    for i in review_list:
        if i['id'] == review_id:
            return i
    raise HTTPException(status_code=404, detail="Review not found")


@router.put("/review_update/{review_id}", response_model=review.ReviewResponse)
async def update_review(review_id:int, data:review.ReviewCreate):
    for i in review_list:
        if i['id'] == review_id:
            check_book(data.book_id)
            i['book_id'] = data.book_id
            i['reviewer_name'] = data.reviewer_name
            i['rating'] = data.rating
            i['comment'] = data.comment
            return i
    raise HTTPException(status_code=404, detail="Review not found")


@router.patch("/review_patch/{review_id}", response_model=review.ReviewResponse)
async def patch_review(review_id:int, data:review.ReviewUpdate):
    for i in review_list:
        if i['id'] == review_id:
            new_data = data.model_dump(exclude_unset=True)
            if 'book_id' in new_data:
                check_book(new_data['book_id'])
            i.update(new_data)
            return i
    raise HTTPException(status_code=404, detail="Review not found")


@router.delete("/review_delete/{review_id}")
async def delete_review(review_id:int):
    for i in review_list:
        if i['id'] == review_id:
            review_list.remove(i)
            return {"message": "review udalit"}
    raise HTTPException(status_code=404, detail="Review not found")
