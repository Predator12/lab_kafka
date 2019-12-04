import localconfig
from attrdict import AttrDict


class Settings:
    CONFIG = None

    def __init__(self, file_name='server.conf'):
        self.read_conf_file(file_name)

    def read_conf_file(self, file_name, config_group='lab'):
        with open(file_name, 'r') as f:
            config_string = f.read()

        config = localconfig.LocalConfig()
        config.read(config_string)

        params = AttrDict({str(key).upper(): value for key, value in getattr(config, config_group) or {}})

        self.CONFIG = params


settings = Settings()
