import os
# from logging.handlers import TimedRotatingFileHandler

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# LOG SETUP #
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
        'debug_file': {
            'level': 'DEBUG',
            'filename': os.path.join(BASE_DIR, 'db_logs/db_debug.log'),
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'when': 'MIDNIGHT',
        },
        'general_file': {
            'level': 'DEBUG',
            'filename': os.path.join(BASE_DIR, 'db_logs/db_general.log'),
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'when': 'MIDNIGHT',
            'formatter': 'main_formatter'
        },
    },
    'formatters': {
        'main_formatter': {
            'format': '%(levelname)s | %(asctime)s | %(filename)s | %(module)s:%(funcName)s:%(lineno)d | %(message)s',
            'datefmt': "%Y-%m-%d %H:%M:%S",
        },
    },
    'loggers': {
        'general': {
            'handlers': ['general_file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

# LOG SETUP END #

