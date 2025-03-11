import requests
from bs4 import BeautifulSoup
from domain.models.ScrapeJob import ScrapeJob
from domain.models.ScrapeResult import ScrapeResult
from domain.interfaces.ScraperInterface import ScraperInterface

class BeautifulSoupScraper(ScraperInterface):
    def scrape(self, job: ScrapeJob) -> ScrapeResult:
        try:
            url = job.target_urls[0] if job.target_urls else None
            if not url:
                raise ValueError("No URL provided in ScrapeJob")
            response = requests.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")
            # Simple extraction: get page title as an example
            title = soup.title.string if soup.title else "No Title"
            data = {"title": title}
            return ScrapeResult(job_id=job.job_id, data=data, success=True)
        except Exception as e:
            return ScrapeResult(job_id=job.job_id, data=None, success=False, error=str(e))
