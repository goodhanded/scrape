from domain.models.ScrapeJob import ScrapeJob
from domain.models.ScrapeResult import ScrapeResult
from domain.interfaces.RepositoryInterface import RepositoryInterface
from typing import Dict, List

class PostgreSQLScrapingJobRepository(RepositoryInterface):
    def __init__(self):
        # In-memory storage for demo purposes
        self.jobs: Dict[str, ScrapeJob] = {}
        self.results: Dict[str, List[ScrapeResult]] = {}

    def save_job(self, job: ScrapeJob) -> None:
        self.jobs[job.job_id] = job

    def save_result(self, result: ScrapeResult) -> None:
        if result.job_id not in self.results:
            self.results[result.job_id] = []
        self.results[result.job_id].append(result)

    def get_results(self, job_id: str) -> List[ScrapeResult]:
        return self.results.get(job_id, [])
