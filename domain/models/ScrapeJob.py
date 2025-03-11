from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional
import uuid

@dataclass
class ScrapeJob:
    job_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    target_urls: List[str] = field(default_factory=list)
    schedule: Optional[str] = None  # e.g., cron expression or timestamp
    status: str = "pending"
    created_at: datetime = field(default_factory=datetime.utcnow)
