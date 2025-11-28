import os
import yaml
from dotenv import load_dotenv

# 1. Load environment variables from .env
load_dotenv()


def load_yaml_config(path="config/config.yaml"):
    """Load YAML config file into a Python dictionary."""
    with open(path, "r") as f:
        return yaml.safe_load(f)


def get_env_var(name, default=None):
    """Return environment variable or default."""
    return os.getenv(name, default)


def load_settings():
    """Merge YAML config + environment variables into unified settings dict."""

    # Load YAML first
    yaml_config = load_yaml_config()

    # Merge YAML + Env into one clean dictionary
    settings = {
        "default_csv": yaml_config.get("default_csv"),
        "default_top_n": yaml_config.get("default_top_n"),
        "output_dir": yaml_config["paths"]["output_dir"],
        "required_columns": yaml_config["validation"]["required_columns"],
        # Environment variables for AI (future use)
        "openai_api_key": get_env_var("OPENAI_API_KEY"),
        "model_name": get_env_var("MODEL_NAME", "gpt-4.1"),
    }

    return settings
