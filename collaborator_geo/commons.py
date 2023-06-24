from configparser import ConfigParser
import logging
import logging.config
import socket

# Get the configparser object
config_object = ConfigParser()


class UtilsClass:

    @staticmethod
    def logger_config():
        logging.basicConfig(format='%(asctime)s,%(msecs)03d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                            datefmt='%Y-%m-%d:%H:%M:%S',
                            level=logging.DEBUG)

        logger = logging.getLogger(__name__)

        # logging.config.dictConfig({'version': 1, 'disable_existing_loggers': True})

        return logger

    @staticmethod
    def generate_ini_configuration_file():
        # Assume we need 2 sections in the config file, let's call them USERINFO and SERVERCONFIG
        config_object["POSTGRES"] = {
            "pg_user": "demo",
            "pg_pwd": "demo",
            "pg_host": "localhost",
            "pg_port": 5432,
            "database": "demo"
        }

        config_object["GEOSERVER"] = {
            "geo_host": "localhost",
            "geo_user": "admin",
            "geo_pwd": "geoserver",
            "geo_port": 8080
        }

        # Write the above sections to config.ini file
        with open('config.ini', 'w') as conf:
            config_object.write(conf)

    @staticmethod
    def get_machine_ip():
        hostname = socket.getfqdn()
        host = socket.gethostbyname_ex(hostname)[2]

        host_auto = socket.gethostbyname('host.docker.internal')

        return host, host_auto

        # import docker
        #
        # client = docker.DockerClient()
        # container = client.containers.get(container_id_or_name)
        # ip_add = container.attrs['NetworkSettings']['IPAddress']
        # print(ip_add)
