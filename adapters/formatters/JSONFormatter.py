import json
from typing import Any
from domain.models.ScrapeResult import ScrapeResult

class JSONFormatter:
    @staticmethod
    def format(result: ScrapeResult) -> str:
        result_dict: dict[str, Any] = {
            "job_id": result.job_id,
            "data": result.data,
            "success": result.success,
            "error": result.error,
            "timestamp": result.timestamp.isoformat() if result.timestamp else None
        }
        return json.dumps(result_dict, indent=2)
