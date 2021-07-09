import yaml

from exceptions.MissingConfig import MissingConfig


def load_yaml(yaml_file, config=True):
    if config:
        yaml_file = f"config/{yaml_file}"
    with open(yaml_file) as f:
        return yaml.safe_load(f)


def get_config(config_file, key, error=True, default=None):
    try:
        return config_file[key]
    except KeyError:
        if error:
            raise MissingConfig(f"The config {key} is missing")
        else:
            return default
