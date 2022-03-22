from typing import Any, Dict, List, Optional

from ..data_classes._base import RushmoreResponse
from ..data_classes.drilling import RushmoreDrillWells
from ._common import get_all_data


class DrillingAPI:
    def __init__(
        self,
        api_key: str,
        page_size: Optional[int] = 1000,
    ):
        self.report_name: str = "DPR"
        self.api_key = api_key
        self.page_size = page_size

    def _get_data(
        self,
        filter: Optional[str] = None,
    ) -> RushmoreResponse:
        return get_all_data(
            api_key=self.api_key,
            report_name=self.report_name,
            page_size=self.page_size,
            filter=filter,
        )

    def get_raw_data(
        self,
        filter: Optional[str] = None,
    ) -> RushmoreResponse:
        """Retrieves all raw data from Rushmore Drilling Performance Review.

        Args:
            filter: Filtering string according to API specification.

        Returns:
            List of dicts where each dict describes a well in the Drilling
            Performance Review.

        """
        return self._get_data(
            filter=filter,
        )

    def _process_data(self, data: RushmoreResponse):
        cleaned = RushmoreDrillWells(Wells=data["Data"]).dict()
        return cleaned["Abandonments"]

    def get_processed_data(
        self,
        filter: Optional[str] = None,
    ) -> List[Dict[str, Any]]:
        """Retrieves processed data from Rushmore Drilling Performance Review.

        This function filters less valuable data and cleans up inconsistencies.

        Args:
            filter: Filtering string according to API specification.

        Example:

            >>> filter = "Location.Country eq 'Norway'"
            >>> e.drilling.get_processed_data(filter)

        """
        data = self._get_data(
            filter=filter,
        )
        return self._process_data(data)
