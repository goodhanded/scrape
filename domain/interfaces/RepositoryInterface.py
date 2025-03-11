from abc import ABC, abstractmethod
from typing import List
from domain.models.ScrapeJob import ScrapeJob
from domain.models.ScrapeResult import ScrapeResult

class RepositoryInterface(ABC):
    @abstractmethod
    def save_job(self, job: ScrapeJob) -> None:
        pass

    @abstractmethod
    def save_result(self, result: ScrapeResult) -> None:
        pass

    @abstractmethod
    def get_results(self, job_id: str) -> List[ScrapeResult]:
        pass
