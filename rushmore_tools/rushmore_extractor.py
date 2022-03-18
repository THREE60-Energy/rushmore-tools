from typing import Any, Dict, Optional

import requests


class RushmoreExtractor:
    """Class used to extract raw data from the Rushmore API.

    The

    Typical usage:
        e = RushmoreExtractor(${API-KEY}, "CPR")
        data = e.get_all_data()

    Args:
        api_key: The X-API-Key provided to Rushmore participants that
          allows access to the Rushmore API.
        report_name: The target Rushmore Performance Report for pulling
          data. Alternatives include e.g. APR, CPR, DPR and depends on
          which reviews the participant has access to.
        api_version: Optional parameter designating the API version to be
          used when sending requests to the API.
        page_size: Optional parameter that specifies the number of rows
          that will be fetched per page. The current limit is based on
          size. Each response may not exceed 10 MiB.

    Raises:
        ValueError: If the submitted report name is not supported.
    """

    def __init__(
        self,
        api_key: str,
        report_name: str,
        api_version: Optional[str] = "0.1",
        page_size: Optional[int] = 1000,
    ) -> None:
        if report_name.lower() not in ("apr", "cpr", "dpr"):
            raise ValueError(f"Report name {report_name} is not supported.")
        self._report_name = report_name
        self._page_size = page_size
        self._base_url = (
            f"https://data-api.rushmorereviews.com/v{api_version}/wells/{report_name}"
        )
        self._header: dict = {"X-API-key": api_key}

    def _get_data_page(self, page_size: int, page: Optional[int] = 1) -> Dict[str, Any]:
        """Queries data from Rushmore.

        Args:
            page_size: Number of rows requested per page.
            page: The page number that is requested.

        Returns:
            One page of data from Rushmore as a JSON serializable
            dictionary with keys according to the standard API payload.
        """
        url = f"{self._base_url}?page={page}&pageSize={page_size}"
        return requests.get(url=url, headers=self._header).json()

    def _get_wellcount(self):
        return self._get_data_page(1, 1)["TotalWells"]

    def _check_error(self, response: Dict[str, Any]):
        """Simple check for overflow error in response.

        Args:
            response: JSON serializable dictionary from Rushmore API.

        Raises:
            ValueError if page size causes response to overflow.
        """
        try:
            error = response["fault"]["faultstring"]
        except KeyError:
            pass
        else:
            if error == "Body buffer overflow":
                raise ValueError(f"Page size of {self._page_size} is too large.")

    def get_all_data(self) -> list[Dict[str, Any]]:
        """Queries all data from Rushmore.

        For the instantiated performance review, iterates through all
        available pages to query an unfiltered list of rows.

        TODO: Look into improving looping logic.

        Returns:
            A list of dicts that each describe a well in the instantiated
            performance review.
        """
        output = []
        page = 1
        while True:
            print(f"Fetching page {page} from {self._report_name.upper()}")
            response = self._get_data_page(self._page_size, page)
            self._check_error(response)
            print(f"Fetched {len(response['Data'])} rows.")
            output.extend(response["Data"])
            if response["TotalPages"] > page:
                page += 1
            else:
                return output
