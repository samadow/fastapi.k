from fastapi import FastAPI,Query, Path,HTTPException
next_id = 1
cate_id = 1
author_list = [
    {
        "id" : next_id,
        "name" : "ali",
        "country" : "Dushabe",
        "birth_year" : "2006"
        
    }
]

categori_list = [
    {
        "id":cate_id,
        "name":"phone",
        "description": "nnnnnn"
        
    }
]

book_list = []

review_list = []
