worker: celery -A config.celery_app worker -Q default --loglevel=info --concurrency=2
beat: celery -A config.celery_app beat --loglevel=info
flower: celery -A config.celery_app flower --port=$PORT
