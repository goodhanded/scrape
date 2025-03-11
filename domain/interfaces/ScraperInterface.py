from abc import ABC, abstractmethod
from domain.models.ScrapeJob import ScrapeJob
from domain.models.ScrapeResult import ScrapeResult

class ScraperInterface(ABC):
    @abstractmethod
    def scrape(self, job: ScrapeJob) -> ScrapeResult:
        pass
