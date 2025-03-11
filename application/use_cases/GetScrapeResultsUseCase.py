from domain.interfaces.RepositoryInterface import RepositoryInterface
from domain.models.ScrapeResult import ScrapeResult
from typing import List

class GetScrapeResultsUseCase:
    def __init__(self, repository: RepositoryInterface):
        self.repository = repository

    def execute(self, job_id: str) -> List[ScrapeResult]:
        return self.repository.get_results(job_id)
