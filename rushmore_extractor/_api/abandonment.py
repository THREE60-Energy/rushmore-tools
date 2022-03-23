from typing import Any, Dict, List, Optional, Union

from ._common import RushmoreResponse, get_data


class AbandonmentAPI:
    def __init__(
        self,
        api_key: str,
        page_size: Optional[int] = 1000,
    ):
        self.report_name: str = "APR"
        self.api_key = api_key
        self.page_size = page_size

    def get(
        self,
        filter: Optional[str] = None,
        full_response: Optional[bool] = True,
        max_pages: Optional[int] = None,
    ) -> Union[RushmoreResponse, List[Dict[str, Any]]]:
        """Retrieves all raw data from Rushmore Abandonment Performance Review.

        Args:
            filter: Filtering string according to API specification.
            full_response: Pass True to retrieve full response from Rushmore.
              False retrieves only the well data list component.
            max_pages: Optional argument to reduce number of pages retrieved
              from Rushmore, for testing purposes.

        Returns:
            List of dicts where each dict describes a well in the Abandonment
            Performance Review.

        """

        return get_data(
            api_key=self.api_key,
            report_name=self.report_name,
            full_response=full_response,
            page_size=self.page_size,
            filter=filter,
            max_pages=max_pages,
        )
