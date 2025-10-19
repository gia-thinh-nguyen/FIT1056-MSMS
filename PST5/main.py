# main.py
from gui.main_dashboard import launch
# TODO: Import the new admin utilities.
from app.admin_utils import init_logger, backup_data

if __name__ == "__main__":
    launch()