from fastapi import FastAPI
from database.session import get_engine
from api.init_db_router import init_router
from api.insert_data_router import insert_data_router
from api.image_router import image_router
from api.select_router import select_router
from api.select_sort_router import select_sort_router
from api.insert_router import insert_router
from api.edit_router import edit_router

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
app.include_router(image_router, prefix="/api") # image api, handles anything image related... almost made my go insnae
app.include_router(select_router, prefix="/api")
app.include_router(select_sort_router, prefix="/api")
app.include_router(insert_router, prefix="/api") # insert data from frontend to db 
app.include_router(edit_router, prefix="/api") # edit data in db from frontend
