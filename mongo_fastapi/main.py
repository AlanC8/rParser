from typing import List
from fastapi import FastAPI, Depends

from .db import get_db
from .schemas import CategoryTree, CategoryWithProducts

app = FastAPI(title="Category API")

@app.get("/categories", response_model=List[CategoryTree])
async def list_categories(db=Depends(get_db)):
    """Return categories with nested subcategories and product names."""
    result: List[CategoryTree] = []
    cursor = db["categories"].find({"parent_id": None})
    async for cat in cursor:
        sub_cats: List[CategoryWithProducts] = []
        sub_cursor = db["categories"].find({"parent_id": cat["_id"]})
        async for sub in sub_cursor:
            products = await db["products"].find({"category_id": sub["_id"]}).to_list(10)
            sub_cats.append(CategoryWithProducts(
                **sub,
                products=[p["name"] for p in products]
            ))
        result.append(CategoryTree(**cat, subcategories=sub_cats))
    return result
