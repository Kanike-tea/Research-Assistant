"""
Application metrics for monitoring API usage.
"""

from __future__ import annotations


class Metrics:
    """Store API usage statistics."""

    def __init__(self):
        self.total_requests = 0
        self.successful_requests = 0
        self.failed_requests = 0
        self.total_response_time = 0.0

    def record_success(self, response_time: float) -> None:
        """Record a successful API request."""
        self.total_requests += 1
        self.successful_requests += 1
        self.total_response_time += response_time
    def record_failure(self) -> None:
        """Record a failed API request."""
        self.total_requests += 1
        self.failed_requests += 1
    def get_metrics(self) -> dict:
        """Return current API metrics."""
        average_response_time = (
        self.total_response_time / self.successful_requests
        if self.successful_requests > 0
        else 0.0
    )
        return {
        "total_requests": self.total_requests,
        "successful_requests": self.successful_requests,
        "failed_requests": self.failed_requests,
        "average_response_time": round(average_response_time, 2),
       }
# Global metrics instance
metrics = Metrics()