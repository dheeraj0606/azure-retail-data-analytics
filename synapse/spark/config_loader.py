import yaml


def load_config(path: str):
    """
    Load YAML configuration files.
    Used for environment-based configs.
    """

    with open(path, "r") as file:
        config = yaml.safe_load(file)

    return config
