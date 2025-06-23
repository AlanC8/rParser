This example demonstrates how to expose categories stored in MongoDB via FastAPI.

Run with:

```
uvicorn mongo_fastapi.main:app
```

The `/categories` endpoint returns categories with nested subcategories and the first few product names for each subcategory.
