import logging
from typing import Any, Dict, List, Optional

import requests

from ._api.abandonment import AbandonmentAPI

logger = logging.getLogger(__name__)


class RushmoreExtractor:
    """Class used to extract raw data from the Rushmore API.

    Typical usage:
        e = RushmoreExtractor(${API-KEY}, "CPR")
        data = e.get_all_data()

    Args:
        api_key: The X-API-Key provided to Rushmore participants that
          allows access to the Rushmore API.

    Raises:
        ValueError: If the submitted report name is not supported.
    """

    def __init__(
        self,
        api_key: str,
    ) -> None:
        self.abandonment = AbandonmentAPI(api_key)
        self.drilling = None
        self.completion = None
