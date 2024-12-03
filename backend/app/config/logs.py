import logging
import logging.config
import os

# Ensure the log directory exists
log_dir = "log"
os.makedirs(log_dir, exist_ok=True)

# Logging configuration
LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        },
    },
    'handlers': {
        'debug_file_handler': {
            'class': 'logging.FileHandler',
            'level': 'DEBUG',
            'formatter': 'default',
            'filename': os.path.join(log_dir, 'debug.log'),
            'mode': 'a',
        },
        'info_file_handler': {
            'class': 'logging.FileHandler',
            'level': 'INFO',
            'formatter': 'default',
            'filename': os.path.join(log_dir, 'info.log'),
            'mode': 'a',
        },
        'warning_file_handler': {
            'class': 'logging.FileHandler',
            'level': 'WARNING',
            'formatter': 'default',
            'filename': os.path.join(log_dir, 'warning.log'),
            'mode': 'a',
        },
        'error_file_handler': {
            'class': 'logging.FileHandler',
            'level': 'ERROR',
            'formatter': 'default',
            'filename': os.path.join(log_dir, 'error.log'),
            'mode': 'a',
        },
        'critical_file_handler': {
            'class': 'logging.FileHandler',
            'level': 'CRITICAL',
            'formatter': 'default',
            'filename': os.path.join(log_dir, 'critical.log'),
            'mode': 'a',
        },
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'default',
            'stream': 'ext://sys.stdout'
        }
    },
    'loggers': {
        '': {  # Root logger
            'level': 'DEBUG',
            'handlers': [
                'debug_file_handler',
                'info_file_handler',
                'warning_file_handler',
                'error_file_handler',
                'critical_file_handler',
                'console'
            ]
        }
    }
}

# Apply logging configuration
logging.config.dictConfig(LOGGING_CONFIG)

# Sample logging
logger = logging.getLogger(__name__)
logger.debug("This is a debug message.")
logger.info("This is an info message.")
logger.warning("This is a warning message.")
logger.error("This is an error message.")
logger.critical("This is a critical message.")
