import unittest
from domain.models.ScrapeJob import ScrapeJob
from domain.models.ScrapeResult import ScrapeResult
from datetime import datetime

class TestDomainModels(unittest.TestCase):
    def test_scrape_job_creation(self):
        job = ScrapeJob(target_urls=["http://example.com"], schedule="* * * * *")
        self.assertIsNotNone(job.job_id)
        self.assertEqual(job.status, "pending")
        self.assertEqual(job.target_urls, ["http://example.com"])
        self.assertEqual(job.schedule, "* * * * *")
        self.assertIsNotNone(job.created_at)

    def test_scrape_result_creation(self):
        result = ScrapeResult(job_id="123", data={"key": "value"}, success=True)
        self.assertEqual(result.job_id, "123")
        self.assertEqual(result.data, {"key": "value"})
        self.assertTrue(result.success)
        self.assertIsNone(result.error)
        self.assertIsInstance(result.timestamp, datetime)

if __name__ == '__main__':
    unittest.main()
