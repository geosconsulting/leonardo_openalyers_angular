from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from configparser import ConfigParser
from collaborator_geo.geoserver_actions import GeoserverClass
from collaborator_geo.geoserver_actions import UtilsClass
import uvicorn


logger = UtilsClass.logger_config()

# Read config.ini file
config_object = ConfigParser()
config_object.read("config.ini")

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:4200",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

geoserver_instance = GeoserverClass('localhost')


@app.get("/workspaces")
async def root():
    geoserver_instance.list_workspaces()
    logger.debug(geoserver_instance.stored_workspaces)
    return {"Workspaces": f"{geoserver_instance.stored_workspaces}"}


@app.get("/layers")
async def layers(user_name: str = 'fabiolana'):
    geoserver_instance.working_workspace = user_name
    lst_layers = geoserver_instance.get_layers()
    lst_layers_filtered = []
    for lyr in lst_layers:
        if user_name in lyr['href']:
            lst_layers_filtered.append(lyr['name'])
    logger.debug(lst_layers_filtered)
    return {"Layers": f"{lst_layers_filtered}"}


if __name__ == "__main__":
    uvicorn.run("main:app", port=5000, log_level="info")
