from typing import List
from geo.Geoserver import Geoserver,GeoserverException
from .commons import UtilsClass

logger = UtilsClass.logger_config()


class GeoserverClass:

    def __init__(self, host, username='admin', password='geoserver'):

        self.host = host
        geoserver_string = f'http://{host}:8080/geoserver'
        self.geoserver_instance = Geoserver(geoserver_string, username=username, password=password)
        self.stored_workspaces = []
        self.stored_styles = []
        self.working_workspace = None

    def list_workspaces(self) -> None:
        """
        List workspaces for checking if already exists
        :return: Nothing
        """
        self.stored_workspaces = []
        workspaces = self.geoserver_instance.get_workspaces()
        for workspace in workspaces['workspaces']['workspace']:
            self.stored_workspaces.append(workspace['name'])

    def get_workspaces(self):
        return self.stored_workspaces

    @property
    def working_workspace(self) -> str:
        return self._working_workspace

    @working_workspace.setter
    def working_workspace(self, workspace_name: str) -> None:
        """

        :param workspace_name: Name of the workspace active during the session
        :return: Nothing
        """
        self._working_workspace = workspace_name

    def workspace_creation(self, workspace_name: str = 'demo') -> None:
        """
        :param workspace_name: Name of the new workspace to be created
        :return: Nothing
        """
        # Creating workspace
        self.geoserver_instance.create_workspace(workspace=workspace_name)

        # Created workspace is set as the activate one
        self.working_workspace = workspace_name

    def workspace_deletion(self) -> None:
        """
        Deleting the active workspace
        :return: Nothing
        """
        # Delete
        self.geoserver_instance.delete_workspace(workspace=self.working_workspace)

    def create_postgis_store(self, store_name, db, pg_user, pg_password, pg_table, title, host='localhost'):
        """
        Publishing a PostGIS table as layer (featurestore)
        :param host: geoserver host
        :param store_name: Store linked to the PostgreSQL/PostGIS database
        :param workspace: workspace chose to contain the layer
        :param db: database containing the table to be published
        :param pg_user: Postgres username
        :param pg_password: Postgres password
        :param pg_table: Postgres table to be published
        :param title: Title of the resulting layer
        :return: Nothing
        """

        # For creating postGIS connection and publish postGIS table
        try:
            self.geoserver_instance.create_featurestore(store_name=store_name, workspace=self.working_workspace, db=db,
                                                        host=host, pg_user=pg_user, pg_password=pg_password)
        except GeoserverException as e:
            logger.error(e.message)

        # For publishing postGIS future store
        try:
            self.geoserver_instance.publish_featurestore(workspace=self.working_workspace, store_name=store_name,
                                                         pg_table=pg_table, title=title)
        except GeoserverException as e:
            logger.error(e.message)

    def upload_associate_style(self, style_path: str = 'styles/collaboration_layer.sld') -> None:
        """
        Upload an existing SLD file and associate it to a featurestore
        :param style_path: path where the SLD file is kept
        :return:
        """

        # For uploading SLD file and connect it with layer
        extract_layer_id = style_path.split('.'[0])[0].split('/')[1]

        try:
            self.geoserver_instance.upload_style(path=style_path, workspace=self.working_workspace)
        except GeoserverException as e:
            logger.error(e.message)

        try:
            self.geoserver_instance.publish_style(layer_name=extract_layer_id, style_name=extract_layer_id,
                                                  workspace=self.working_workspace)
        except GeoserverException as e:
            logger.error(e.message)

    def list_styles(self) -> None:
        styles = self.geoserver_instance.get_styles()
        for style in styles:
            print(style)
            # self.stored_styles.append(style['name'])

    def get_styles(self):
        return self.stored_styles

    def create_raster_store(self, layer_name, path, workspace) -> None:
        """
        For uploading raster data to the geoserver
        :param layer_name: name assigned to the coverage store
        :param path: where the raster is stored
        :param workspace: where to assign the raster
        :return: Nothing
        """

        self.geoserver_instance.create_coveragestore(layer_name=layer_name, path=path, workspace=workspace)

    def get_layers(self) -> List:
        layers_for_working_ws = self.geoserver_instance.get_layers(self.working_workspace)
        return layers_for_working_ws['layers']['layer']

    def delete_layer_by_name(self, layer_name: str = 'collaboration_layer') -> None:
        self.geoserver_instance.delete_layer(layer_name=layer_name, workspace=self.working_workspace)

    def delete_style_by_name(self, style_name: str = 'collaboration_layer') -> None:
        self.geoserver_instance.delete_style(style_name=style_name, workspace=self.working_workspace)
