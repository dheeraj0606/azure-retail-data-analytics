import os


def get_env_variable(name: str, default=None):
    """
    Fetch environment variables with optional default.
    Useful for secrets/config.
    """
    value = os.getenv(name, default)

    if value is None:
        raise ValueError(f"Environment variable {name} not set")

    return value
