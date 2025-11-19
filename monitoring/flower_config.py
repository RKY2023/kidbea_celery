"""
Flower Dashboard Configuration for Celery monitoring

Access at: https://[your-railway-url]:5555
Login: admin / [password from FLOWER_BASIC_AUTH env var]
"""

import os

# ===== Flower Basic Configuration =====

# Port to run Flower on
FLOWER_PORT = int(os.getenv('PORT', 5555))

# Basic authentication (required for security)
# Format: "username:password"
FLOWER_BASIC_AUTH = [os.getenv('FLOWER_BASIC_AUTH', 'admin:password')]

# ===== Broker Configuration =====

# Celery broker API for Flower to connect to
FLOWER_BROKER_API = os.getenv('CELERY_BROKER_URL', 'redis://localhost:6379/0')

# ===== Persistence =====

# Database file for Flower persistence
FLOWER_DB = '/tmp/flower.db'

# Persist data between restarts
FLOWER_PERSISTENT = True

# ===== Task Management =====

# Maximum number of tasks to display in Flower
FLOWER_MAX_TASKS = 10000

# Update interval for real-time data (milliseconds)
FLOWER_UPDATE_INTERVAL = 5000

# ===== Display Settings =====

# Log level
FLOWER_LOGGING = os.getenv('FLOWER_LOGGING', 'info')

# Refresh rate (milliseconds)
FLOWER_REFRESH_TIME = 1000

# ===== Security =====

# List of allowed origins for CORS
FLOWER_CONF = {
    'max_tasks': FLOWER_MAX_TASKS,
    'persistent': FLOWER_PERSISTENT,
    'db': FLOWER_DB,
}

# ===== Additional Settings =====

# Enable Flower stats
FLOWER_ENABLE_STATS = True

# Enable Flower state dump
FLOWER_ENABLE_STATE_DUMP = True

# Auto-reload on changes (disabled in production)
FLOWER_AUTORELOAD = os.getenv('DEBUG', 'False') == 'True'
