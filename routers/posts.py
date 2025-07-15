from fastapi import APIRouter, Query, status
from fastapi.responses import JSONResponse
from typing import List, Optional
from models.post import BlogPost, TagSearchError
from utils.tags import ALLOWED_TAGS, filter_posts_by_tags, validate_tags

# In-memory dummy data for demonstration
DUMMY_POSTS = [
    BlogPost(id=1, title="Async Python", tags=["python", "asyncio"]),
    BlogPost(id=2, title="FastAPI Tips", tags=["python", "fastapi"]),
    BlogPost(id=3, title="Frontend Love", tags=["react", "javascript"]),
    BlogPost(id=4, title="Concurrency Deep Dive", tags=["asyncio", "concurrency"]),
]

router = APIRouter()

@router.get("/search", response_model=List[BlogPost], responses={
    422: {
        "model": TagSearchError,
        "description": "Invalid tags provided"
    }
})
async def search_posts(tags: Optional[str] = Query(None, description="Comma-separated list of tags")):
    if not tags:
        return DUMMY_POSTS
    tag_list = [tag.strip() for tag in tags.split(",") if tag.strip()]
    invalid_tags = validate_tags(tag_list)
    if invalid_tags:
        error = TagSearchError(
            detail="Invalid tags provided.",
            invalid_tags=invalid_tags
        )
        return JSONResponse(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, content=error.dict())
    filtered = filter_posts_by_tags(DUMMY_POSTS, tag_list)
    return filtered
