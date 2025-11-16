from fastapi import FastAPI
from database.session import get_engine
from api.init_db_router import init_router
from api.insert_data_router import insert_data_router
from api.image_router import image_router


async def lifespan(app: FastAPI):
    engine = get_engine(testing=True)  # Use testing sqlite DB by default
    app.state.engine = engine
    yield
    await engine.dispose()


app = FastAPI(
    lifespan=lifespan,
    openapi_tags=[
        {"name": "List", "description": "anything that has to do with listing data"},
        {"name": "Find", "description": "anything that is related to find"},
        {"name": "Initialize", "description": "initialize all tables into the db :D"},
    ],
)



app.include_router(init_router, prefix="/api/init")  # initialize db tables
app.include_router(insert_data_router, prefix="/api/init")  # insert data into db
app.include_router(image_router, prefix="/api/test") # testapi :p