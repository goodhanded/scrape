from domain.models.ScrapeJob import ScrapeJob
from domain.models.ScrapeResult import ScrapeResult
from domain.interfaces.ScraperInterface import ScraperInterface
from domain.interfaces.RepositoryInterface import RepositoryInterface

class StartScrapingUseCase:
    def __init__(self, scraper: ScraperInterface, repository: RepositoryInterface):
        self.scraper = scraper
        self.repository = repository

    def execute(self, job: ScrapeJob) -> ScrapeResult:
        # Save the job
        self.repository.save_job(job)
        # Perform scraping
        result = self.scraper.scrape(job)
        # Save the result
        self.repository.save_result(result)
        return result
