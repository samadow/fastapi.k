from fastapi import FastAPI
from routers import authors, categories, books, reviews

app = FastAPI(title='saidjafar')

app.include_router(authors.router)
app.include_router(categories.router)
app.include_router(books.router)
app.include_router(reviews.router)





