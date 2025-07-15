from celery import Celery
from app.config import settings

celery_app = Celery("notification_service")
celery_app.conf.broker_url = settings.celery_broker_url
celery_app.conf.result_backend = settings.celery_result_backend
celery_app.conf.task_routes = {
    "send_notification_task": {"queue": "sms_queue"},
}

celery_app.autodiscover_tasks(["app.workers"])
