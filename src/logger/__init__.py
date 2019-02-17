import logging.config
from .config import LOGGING

# Configurations logger dictionary file
logging.config.dictConfig(LOGGING)

# Initiated the logging file to variable
logger_file = logging
