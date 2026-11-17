import pika
from dotenv import load_dotenv
import logging
import os
from pathlib import Path


# -------------------------------------------
# Variables
# -------------------------------------------

VHOST = "%2F"

# -------------------------------------------
# Helper functions
# -------------------------------------------

def requirements():
    """Loads the requirements"""
    load_dotenv()
    rabbitmq_user = os.getenv("RABBITMQ_USER")
    rabbitmq_passwd = os.getenv("RABBITMQ_PASSWD")
    script_dir = Path(__file__).resolve().parent
    log_dir = script_dir / "logs"
    log_dir.mkdir(parents=True, exist_ok=True)
    log_file = log_dir / "app.log"

    logging.basicConfig(
    filename=log_file,
    filemode="a",
    encoding="utf-8"
    )

    return rabbitmq_passwd, rabbitmq_user

def create_queue():
    """Create a queue"""
    
