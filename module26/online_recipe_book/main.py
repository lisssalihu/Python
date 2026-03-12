from fastapi import FastAPI
from database import engine
from models import recipe, category
from routers import recipes, categories

app = FastAPI(title="Recipe API")

recipe.Base.metadata.create_all(bind=engine)
category.Base.metadata.create_all(bind=engine)

app.include_router(recipes.router)
app.include_router(categories.router)