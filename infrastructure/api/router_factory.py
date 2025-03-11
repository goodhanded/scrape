from fastapi import APIRouter, HTTPException
from infrastructure.api.schemas import ScrapeJobRequest, ScrapeResultResponse
from domain.models.ScrapeJob import ScrapeJob
from application.use_cases.StartScrapingUseCase import StartScrapingUseCase


class RouterFactory:
    def __init__(self, start_scraping_use_case: StartScrapingUseCase):
        self.start_scraping_use_case = start_scraping_use_case

    def start_scrape(self, job_request: ScrapeJobRequest) -> ScrapeResultResponse:
        
        # Create a ScrapeJob from the request data
        job = ScrapeJob(target_urls=job_request.target_urls, schedule=job_request.schedule)
        
        # Execute the scraping use case
        result = self.start_scraping_use_case.execute(job)
        
        if not result.success:
            raise HTTPException(status_code=400, detail=result.error)
        
        return result

    def create(self) -> APIRouter:
        router = APIRouter()
        router.add_api_route(
            "/jobs",
            self.start_scrape,
            methods=["POST"],
            response_model=ScrapeResultResponse
        )
