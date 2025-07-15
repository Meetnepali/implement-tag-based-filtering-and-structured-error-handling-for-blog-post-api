# Allowed tags for the blog system
ALLOWED_TAGS = {"python", "asyncio", "fastapi", "react", "javascript", "concurrency"}

def validate_tags(tags):
    """Return a list of invalid tags (not in allowed set)"""
    return [t for t in tags if t not in ALLOWED_TAGS]

def filter_posts_by_tags(posts, tags):
    """Return posts that have ANY of the requested tags"""
    return [post for post in posts if set(post.tags) & set(tags)]
