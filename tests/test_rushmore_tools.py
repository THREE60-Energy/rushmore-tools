import pytest

from rushmore_tools import __version__
from rushmore_tools.rushmore_extractor import RushmoreExtractor


def test_version():
    assert __version__ == "0.1.0"


def test_rushmore_error_check_with_error():
    response_dict = {"fault": {"faultstring": "Body buffer overflow"}}
    Test = RushmoreExtractor("ABC", "CPR")
    with pytest.raises(ValueError):
        Test._check_error(response_dict)
    with pytest.raises(ValueError):
        RushmoreExtractor("ABC", "INVALID")


def test_rushmore_error_checks_without_error():
    Test = RushmoreExtractor("ABC", "CPR")

    assert Test._report_name == "CPR"
    assert Test._base_url == "https://data-api.rushmorereviews.com/v0.1/wells/CPR"
    assert Test._page_size == 1000
    assert Test._check_error({"whatever": "test"}) is None
