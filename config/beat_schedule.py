"""
All scheduled tasks for Celery Beat
Scheduled to run on Railway's kidbea_celery service

These tasks are routed to the correct workers via task routing:
- Data collection tasks (weather, trends, festivals) → ml_tasks queue → kidbea_ml worker
- ML tasks (forecasting, accuracy, alerts) → ml_tasks queue → kidbea_ml worker
"""

from celery.schedules import crontab

CELERY_BEAT_SCHEDULE = {
    # ===== Data Collection (ML Worker) =====
    'collect-weather-data': {
        'task': 'forecasting.tasks.collect_weather_data',
        'schedule': crontab(hour=6, minute=0),  # Daily at 6 AM
        'options': {'queue': 'ml_tasks'}
    },
    'collect-trends-data': {
        'task': 'forecasting.tasks.collect_trends_data',
        'schedule': crontab(hour=7, day_of_week=0, minute=0),  # Weekly on Sundays at 7 AM
        'options': {'queue': 'ml_tasks'}
    },
    'update-festival-calendar': {
        'task': 'forecasting.tasks.update_festival_calendar',
        'schedule': crontab(hour=0, day_of_month=1, minute=0),  # Monthly on 1st at midnight
        'options': {'queue': 'ml_tasks'}
    },

    # ===== ML Tasks (Forecasting) =====
    'train-forecast-models': {
        'task': 'forecasting.tasks.train_all_skus',
        'schedule': crontab(hour=22, minute=0),  # Weekly on Sunday at 10 PM
        'options': {'queue': 'ml_tasks'}
    },
    'generate-daily-forecasts': {
        'task': 'forecasting.tasks.generate_forecasts',
        'schedule': crontab(hour=2, minute=0),  # Daily at 2 AM
        'options': {'queue': 'ml_tasks'}
    },
    'calculate-forecast-accuracy': {
        'task': 'forecasting.tasks.calculate_accuracy',
        'schedule': crontab(hour=3, minute=0),  # Daily at 3 AM
        'options': {'queue': 'ml_tasks'}
    },
    'generate-inventory-alerts': {
        'task': 'forecasting.tasks.generate_alerts',
        'schedule': crontab(hour=4, minute=0),  # Daily at 4 AM
        'options': {'queue': 'ml_tasks'}
    },
}
