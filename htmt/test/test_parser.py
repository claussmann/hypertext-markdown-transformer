import pytest
from htmt.parser import *
from .html_resources import *


def test_parser_simple():
    parser = HTMT_Parser(loglevel="NO_LOG")
    assert parser.markdownify(html1) == makrdown1