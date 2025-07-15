# Guide to the Project

This project is a minimal FastAPI-based blog post API, focusing **specifically** on a tag-based filtering feature with error handling. The environment is streamlined for a technical assessment focusing only on the tag filtering, validation, and error response logic for the `/posts/search` endpoint.

## Assessment Requirements
- Implement or update the `/posts/search` GET endpoint in the provided router, accepting a comma-separated `tags` query parameter (e.g., `/posts/search?tags=python,asyncio`).
- Only tags from a predefined set (see util file) are valid. If any supplied tag(s) are invalid, the API must return a **structured 422 response** (JSON), listing each invalid tag and using the specified Pydantic error model.
- The codebase includes only dummy in-memory data. You should focus **entirely** on: filtering logic, request validation, modular design, and appropriate error handling/schema usage.
- All relevant changes should be limited to the router, Pydantic models, or the utility code (no database, no authentication, no unrelated features).
- The API must be async and follow FastAPI best practices for modularity and validation.
- All core logic must be easy to test and reason about.

## Files/Folders to Focus On
- `routers/posts.py`: Where endpoint logic and filtering will go.
- `models/post.py`: Where response and error schemas are defined.
- `utils/tags.py`: Provides the allowed tag set, filtering and validation helpers.

## What NOT to Change
- Do not touch authentication, persistent storage, unrelated endpoints, Dockerfile, or run/install scripts.
- Do not introduce architectural changes (e.g., dependency injection, app-wide config).

## Verifying Your Solution
- Compose a GET request to `/posts/search?tags=python,asyncio`.
  - On valid tags, response is a JSON list of posts matching any selected tag.
  - On one or more **invalid tags** (e.g. `/posts/search?tags=python,unknown`), response is HTTP 422, with the invalid tags clearly listed in the error structure.
- The endpoint should be async, modular, straightforward, and robust.
- Only the specifically-requested functionality should be implemented or changed.

---

**Aim for clarity, modularity, correct use of FastAPI and Pydantic, and the exact error semantics described above.**