import pytest
from requests_mock import Mocker

from rushmore_tools._api.api import (
    RushmoreReport,
    _check_response,
    get_data,
    get_data_page,
)
from rushmore_tools.rushmore_extractor import RushmoreExtractor
from rushmore_tools.utils.conversion_functions import hole_type, rig_type, well_type


def test_check_response():
    response_dict_ok = {"TotalWells": 123, "Data": {"More stuff"}}
    response_dict_fault = {"fault": {"faultstring": "Body buffer overflow"}}
    response_dict_error = {"error": "blah", "error_description": "major error"}

    # Checking for regular response
    assert _check_response(response_dict_ok) == None

    # Checking for body overflow (response too large)
    with pytest.raises(ValueError):
        _check_response(response_dict_fault)
        assert ValueError == "Response too large. Reduce page size."

    # Blanket test for errors raised
    with pytest.raises(Exception):
        _check_response(response_dict_error)
        assert (
            Exception == f"Error was thrown: {response_dict_error['error_description']}"
        )


def test_rig_type():
    assert rig_type("") == ("N/A", False)
    assert rig_type("LA  ") == ("Land rig (Rented)", False)
    assert rig_type("SS (2)") == ("Semi-submersible", True)
    assert rig_type("SS (2) PL") == ("Several", True)
    assert rig_type("TS SS (2)") == ("Semi-submersible", True)
    assert rig_type("BA TB ") == ("Barge", False)
    assert rig_type("TJ  JK  ") == ("Jack-up", False)
    with pytest.raises(ValueError):
        rig_type("Splerg")
        assert ValueError == "Rig type designation 'Splerg' is unknown."


def test_hole_type():
    assert hole_type("N") == "New well"
    assert hole_type("n") == "New well"
    assert hole_type("g") == "Geological sidetrack"
    assert hole_type("s") == "Slot recovery"
    assert hole_type("o") == "Other"
    assert hole_type("foo") == None


def test_well_type():
    assert well_type("e") == "Exploration"
    assert well_type("foo") == None


def test_rushmore_report(requests_mock: Mocker):
    # Instantiating class
    api_key = "ABC"
    page_size = 100
    a = RushmoreReport("APR", api_key, page_size)

    # Testing basic properties
    assert a.api_key == api_key
    assert a.page_size == page_size
    assert a.report_name == "APR"

    # Testing get function
    url = f'https://data-api.rushmorereviews.com/v0.1/wells/{a.report_name}?page=1&pageSize={page_size}&filter=Location.Country eq "Norway"'
    response = {"TotalPages": 1, "Data": "Hello World"}
    requests_mock.get(url, json=response)
    assert response["Data"] == a.get(
        data_filter='Location.Country eq "Norway"',
        full_response=False,
    )

    # Testing page size setter
    with pytest.raises(ValueError):
        a.page_size = -1
    with pytest.raises(TypeError):
        a.page_size = 2.3
    with pytest.raises(TypeError):
        a.page_size = "Hello"

    # Checking that valid size raises exception
    try:
        a.page_size = 4
    except:
        assert False, f"Setter raised exception."


def test_get_data_page(requests_mock: Mocker):
    url = 'https://data-api.rushmorereviews.com/v0.1/wells/APR?page=1&pageSize=1&filter=Location.Country eq "Norway"'
    response = {"Hello": "World", "Key": 123}
    requests_mock.get(url, json=response)
    assert response == get_data_page(
        api_key="ABC",
        report_name="APR",
        page=1,
        page_size=1,
        data_filter='Location.Country eq "Norway"',
    )


def test_get_data(requests_mock: Mocker):
    # Parameters
    _filter = 'Location.Country eq "Norway"'
    _page_size = 2
    _report_name = "APR"

    # Response mocking
    url1 = f"https://data-api.rushmorereviews.com/v0.1/wells/{_report_name}?page=1&pageSize={_page_size}&filter={_filter}"
    url2 = f"https://data-api.rushmorereviews.com/v0.1/wells/{_report_name}?page=2&pageSize={_page_size}&filter={_filter}"
    url3 = f"https://data-api.rushmorereviews.com/v0.1/wells/{_report_name}?page=3&pageSize={_page_size}&filter={_filter}"
    page1 = {"Stuff": "Foo", "TotalPages": 3, "Data": [1, 2]}
    page2 = {"Stuff": "Foo", "TotalPages": 3, "Data": [3, 4]}
    page3 = {"Stuff": "Foo", "TotalPages": 3, "Data": [5, 7]}
    requests_mock.get(url1, json=page1)
    requests_mock.get(url2, json=page2)
    requests_mock.get(url3, json=page3)

    full_response = {"Stuff": "Foo", "TotalPages": 3, "Data": [1, 2, 3, 4]}
    partial_response = full_response["Data"]
    all_pages = [1, 2, 3, 4, 5, 7]

    assert full_response == get_data(
        api_key="ABC",
        report_name=_report_name,
        full_response=True,
        page_size=_page_size,
        max_pages=2,
        data_filter=_filter,
    )

    assert partial_response == get_data(
        api_key="ABC",
        report_name=_report_name,
        full_response=False,
        page_size=2,
        max_pages=2,
        data_filter=_filter,
    )

    assert all_pages == get_data(
        api_key="ABC",
        report_name=_report_name,
        full_response=False,
        page_size=2,
        data_filter=_filter,
    )


def test_extractor():
    e = RushmoreExtractor("ABC")

    assert e.abandonment.api_key == "ABC"
    assert e.completion.api_key == "ABC"
    assert e.drilling.api_key == "ABC"
