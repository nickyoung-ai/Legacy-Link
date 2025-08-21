# Legacy-Link
platform for real voices, real vibes, and real vaule
Legacy Link is a revolutionary short-form video platform built with **FastAPI**, **PostgreSQL**, and modern web technologies.
It empowers authentic voices to connect ,create , and compete through features like live battles , Sprite gifting, and more.

- - -
Features
- **Face-Off Mode**-1 or 3 mintue live battles beteewn creators.
- **Sprite Gifting System**- Digital gifts ranging from $0.01 to $300.
-**Legacy Layer** Profile and History tracking.
-**Drop Zone ** Timed content drops
**LightChain**- Token system for rewards.
-**RWT (Real World Tasks)**- Challenges that reward impact and authenticity.
---
## Project Structure
/legacy_link #App package(routers, schemas, models, ect)
main.py #FastAPI entry point
database.py #Database connection
(PostgreSQL)
models.py #SQLAlchemy models
schemas.py #Pydantic schemas
router/ #API routes(auth,porfiles, faceoff, ect.)
alembic/ #Database migrations
README.md #Project documentation
LICENSE #License info