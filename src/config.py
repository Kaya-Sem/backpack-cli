import os

def get_xdg_config_home():
    """XDG config home directory, defaulting to ~/.config if not set."""
    return os.getenv('XDG_CONFIG_HOME', os.path.expanduser('~/.config'))

def ensure_project_directory(project_name):
    """Ensure configuration directory exists."""
    xdg_config_home = get_xdg_config_home()
    project_dir = os.path.join(xdg_config_home, project_name)
    os.makedirs(project_dir, exist_ok=True)
    return project_dir

def get_database_path():
    """Construct and return the path to the SQLite database."""
    project_name = 'backpack-cli'
    project_dir = ensure_project_directory(project_name)
    return os.path.join(project_dir, 'database.sqlite')
