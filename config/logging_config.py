"""
Logging configuration for Celery worker and Flower
"""

import logging
import sys

# Configure root logger
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    stream=sys.stdout
)

# Get loggers
celery_logger = logging.getLogger('celery')
beat_logger = logging.getLogger('celery.beat')
flower_logger = logging.getLogger('flower')

# Set levels
celery_logger.setLevel(logging.INFO)
beat_logger.setLevel(logging.INFO)
flower_logger.setLevel(logging.INFO)
