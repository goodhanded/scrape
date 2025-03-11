from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Optional

@dataclass
class ScrapeResult:
    job_id: str
    data: Any
    success: bool = True
    error: Optional[str] = None
    timestamp: datetime = field(default_factory=datetime.utcnow)
