import os
import time
from typing import Any

from celery import Celery

broker_url = os.getenv("CELERY_BROKER_URL", os.getenv("REDIS_URL", "redis://localhost:6379/0"))
result_backend = os.getenv("CELERY_RESULT_BACKEND", "redis://localhost:6379/1")

celery_app = Celery("impactproof_worker", broker=broker_url, backend=result_backend)
celery_app.conf.task_default_queue = "impactproof"


@celery_app.task(name="impactproof.extract_and_score")
def extract_and_score(payload: dict[str, Any]) -> dict[str, Any]:
    """Placeholder background task for future extraction/scoring pipeline.

    TODO: integrate provider adapters / LLM calls and persist results through backend domain services.
    """
    time.sleep(1)
    text = str(payload.get("content", ""))
    return {
        "status": "completed",
        "category": "Operational Improvement",
        "impact_score": min(max(len(text) / 100.0, 1.0), 10.0) if text else None,
        "summary": (text[:200] + "...") if len(text) > 200 else text,
    }
