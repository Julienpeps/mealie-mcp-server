from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field


class RecipeIngredient(BaseModel):
    quantity: Optional[float] = 0
    unit: Optional[str] = None
    food: Optional[str] = None
    note: Optional[str] = ""
    isFood: Optional[bool] = True
    disableAmount: Optional[bool] = False
    display: Optional[str] = ""
    title: Optional[str] = None
    originalText: Optional[str] = None
    referenceId: Optional[str] = None


class RecipeInstruction(BaseModel):
    id: Optional[str] = None
    title: Optional[str] = ""
    summary: Optional[str] = ""
    text: str
    ingredientReferences: List[str] = Field(default_factory=list)


class RecipeNutrition(BaseModel):
    calories: Optional[str] = None
    carbohydrateContent: Optional[str] = None
    cholesterolContent: Optional[str] = None
    fatContent: Optional[str] = None
    fiberContent: Optional[str] = None
    proteinContent: Optional[str] = None
    saturatedFatContent: Optional[str] = None
    sodiumContent: Optional[str] = None
    sugarContent: Optional[str] = None
    transFatContent: Optional[str] = None
    unsaturatedFatContent: Optional[str] = None


class RecipeSettings(BaseModel):
    public: bool = False
    showNutrition: bool = False
    showAssets: bool = False
    landscapeView: bool = False
    disableComments: bool = True
    disableAmount: bool = False
    locked: bool = False


class Recipe(BaseModel):
    id: Optional[str] = None
    userId: str
    householdId: str
    groupId: str
    name: Optional[str] = None
    slug: str = ""
    image: Optional[str] = None
    recipeServings: float = 0
    recipeYieldQuantity: float = 0
    recipeYield: Optional[str] = None
    totalTime: Optional[str] = None
    prepTime: Optional[str] = None
    cookTime: Optional[str] = None
    performTime: Optional[str] = None
    description: Optional[str] = ""
    recipeCategory: List[str] = Field(default_factory=list)
    tags: List[str] = Field(default_factory=list)
    tools: List[str] = Field(default_factory=list)
    rating: Optional[float] = None
    orgURL: Optional[str] = None
    dateAdded: Optional[str] = None
    dateUpdated: Optional[str] = None
    createdAt: Optional[str] = None
    updatedAt: Optional[str] = None
    lastMade: Optional[str] = None
    recipeIngredient: List[RecipeIngredient] = Field(default_factory=list)
    recipeInstructions: List[RecipeInstruction] = Field(default_factory=list)
    nutrition: Optional[RecipeNutrition] = None
    settings: Optional[RecipeSettings] = None
    assets: List[Any] = Field(default_factory=list)
    notes: List[Any] = Field(default_factory=list)
    extras: Dict[str, Any] = Field(default_factory=dict)
    comments: List[Any] = Field(default_factory=list)
