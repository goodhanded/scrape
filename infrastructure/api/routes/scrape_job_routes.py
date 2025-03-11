from fastapi import APIRouter, HTTPException
from infrastructure.api.schemas import ScrapeJobRequest, ScrapeResultResponse
from domain.models.ScrapeJob import ScrapeJob
from application.use_cases.StartScrapingUseCase import StartScrapingUseCase

router = APIRouter()

@router.post("/jobs", response_model=ScrapeResultResponse)
def start_scrape(job_request: ScrapeJobRequest) -> ScrapeResultResponse:
    # Create a ScrapeJob from the request
    job = ScrapeJob(target_urls=job_request.target_urls, schedule=job_request.schedule)
    #use_case: StartScrapingUseCase = container.start_scraping_use_case  # Get the use case from the container
    result = use_case.execute(job)
    if not result.success:
        raise HTTPException(status_code=400, detail=result.error)
    return result
