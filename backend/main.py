from fastapi import FastAPI
from database.session import get_engine
from router.init_db_router import init_router



async def lifespan(app: FastAPI):

    engine = get_engine(testing=True) # Change tersting to False for the actual, to make everything simple this will utilize a local sqllite db :D

    app.state.engine = engine
    yield
    engine.dispose()

app = FastAPI(
    lifespan=lifespan, 
    openapi_tags=[
        {
        "name": "List",
        "description": "anything that has to do with listing data"
        },
        {
        "name": "Find",
        "description": "anything that is related to find"
        },
        {
        "name": "Initialize",
        "description": "initialize all tables into the db :D"
        }
    ]
)

app.include_router(init_router, prefix="/api") # initialize db tables