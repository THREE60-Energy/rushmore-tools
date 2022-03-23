import logging
import os
from typing import Any, Dict, List, Optional, TypedDict, Union

import requests

logger = logging.getLogger(__name__)


class RushmoreResponse(TypedDict):
    """Type class for Rushmore Response."""

    TotalWells: Optional[int]
    TotalPages: Optional[int]
    PageInfo: Optional[Dict[str, Any]]
    Data: Optional[List[Dict[str, Any]]]


def get_data_page(
    api_key: str,
    report_name: str,
    page_size: int,
    api_version: Optional[str] = "0.1",
    page: Optional[int] = 1,
    filter: Optional[str] = None,
) -> RushmoreResponse:
    """Queries data from Rushmore.

    Args:
        page_size: Number of rows requested per page.
        page: The page number that is requested.
        filter: Custom filters for what data to include.

    Returns:
        One page of data from Rushmore as a JSON serializable
        dictionary with keys according to the standard API payload.
    """
    # Rushmore API uses X-API-key authorization.
    header = {"X-API-key": api_key}
    base_url = (
        f"https://data-api.rushmorereviews.com/v{api_version}/wells/{report_name}"
    )
    url = f"{base_url}?page={page}&pageSize={page_size}"
    if filter:
        url = f"{url}&filter={filter}"

    response = requests.get(
        url=url,
        headers=header,
    )

    # Checks for non-2xx responses
    response.raise_for_status()

    return response.json()


def _check_response(response: RushmoreResponse) -> None:
    """Simple check for overflow error in response.

    Args:
        response: Rushmore API response.

    Raises:
        ValueError if page size causes response to overflow.
    """
    logger.debug("Checking response for error messages.")
    try:
        response["fault"]
    except KeyError:
        pass
    else:
        error: str = response["fault"]["faultstring"]
        if error == "Body buffer overflow":
            raise ValueError(f"Response too large. Reduce page size.")
        else:
            raise Exception(f"Error was thrown: {error}.")
    try:
        response["error"]
    except KeyError:
        pass
    else:
        error: str = response["error_description"]
        raise Exception(f"Error was thrown: {error}.")


def get_data(
    api_key: str,
    report_name: str,
    full_response: Optional[bool] = True,
    page_size: Optional[int] = 1000,
    filter: Optional[str] = None,
    max_pages: Optional[int] = None,
) -> Union[RushmoreResponse, List[Dict[str, Any]]]:
    """Queries all data from Rushmore.

    For the instantiated performance review, iterates through all
    available pages to query an unfiltered list of rows.

    TODO: Look into improving looping logic.

    Args:
        filter: Submit a well-formed filter string according to the Rushmore
            API specification. This filter will be passed to the API.

    Returns:
        A list of dicts that each describe a well in the provided
        performance review.

    Raises:
        ValueError if page size exceeds maximum allowable.
        Exception for other API errors.
    """
    output: Optional[RushmoreResponse] = None
    page = 1
    while True:
        logger.info(f"Fetching page {page} from {report_name.upper()}")
        response = get_data_page(
            api_key=api_key,
            report_name=report_name,
            page_size=page_size,
            page=page,
            filter=filter,
        )

        # Response checker catches error / failure responses
        _check_response(response)

        logger.info(f"Fetched {len(response['Data'])} rows.")
        if output:
            output["Data"].extend(response["Data"])
        else:
            output = response

        # Determine number of pages to fetch. TODO: Revise logic if lightweight API calls are available.
        if not max_pages:
            num_pages = response["TotalPages"]
        else:
            num_pages = min(max_pages, response["TotalPages"])

        if num_pages > page:
            page += 1
        else:
            logger.info(f"Extraction complete. {len(output['Data']):,} rows fetched.")
            if full_response:
                return output
            else:
                return output["Data"]
