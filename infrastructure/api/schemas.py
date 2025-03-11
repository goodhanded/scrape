from pydantic import BaseModel
from datetime import datetime
from typing import Any, Optional

class ScrapeJobRequest(BaseModel):
    target_urls: list[str]
    schedule: Optional[str] = None

class ScrapeResultResponse(BaseModel):
    job_id: str
    data: Any
    success: bool
    error: Optional[str] = None
    timestamp: datetime
