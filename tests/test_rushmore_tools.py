import pytest

from rushmore_tools import __version__
from rushmore_tools.rushmore_extractor import RushmoreExtractor


def test_version():
    assert __version__ == "0.1.0"
