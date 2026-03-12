from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models.recipe import Recipe

router = APIRouter(prefix="/recipes", tags=["Recipes"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
def create_recipe(
        title: str,
        description: str,
        ingredients: str,
        category_id: int,
        db: Session = Depends(get_db)
):

    recipe = Recipe(
        title=title,
        description=description,
        ingredients=ingredients,
        category_id=category_id
    )

    db.add(recipe)
    db.commit()
    db.refresh(recipe)

    return recipe


@router.get("/")
def get_recipes(db: Session = Depends(get_db)):
    return db.query(Recipe).all()