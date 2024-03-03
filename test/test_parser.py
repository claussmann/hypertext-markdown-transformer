import pytest
from htmt.parser import *
from .html_resources import *


def test_parser_general():
    parser = HTMT_Parser(loglevel=LogLevel.NO_LOGS)
    assert parser.markdownify(html_general) == makrdown_general

def test_parser_bold_italic():
    parser = HTMT_Parser(loglevel=LogLevel.NO_LOGS)
    assert parser.markdownify(html_bold_italic) == markdown_bold_italic

def test_parser_headers():
    parser = HTMT_Parser(loglevel=LogLevel.NO_LOGS)
    assert parser.markdownify(html_headers) == markdown_headers

def test_parser_lists():
    parser = HTMT_Parser(loglevel=LogLevel.NO_LOGS)
    assert parser.markdownify(html_lists) == markdown_lists

def test_parser_tables():
    parser = HTMT_Parser(loglevel=LogLevel.NO_LOGS)
    assert parser.markdownify(html_tables) == markdown_tables

def test_parser_links_ignore():
    parser = HTMT_Parser(loglevel=LogLevel.NO_LOGS, linkhandling=LinkHandling.IGNORE)
    assert parser.markdownify(html_links) == markdown_links_ignore

def test_parser_links_reference():
    parser = HTMT_Parser(loglevel=LogLevel.NO_LOGS, linkhandling=LinkHandling.REFERENCE)
    assert parser.markdownify(html_links) == markdown_links_reference

def test_parser_images_ignore():
    parser = HTMT_Parser(loglevel=LogLevel.NO_LOGS, imagehandling=ImageHandling.IGNORE)
    assert parser.markdownify(html_img) == markdown_img_ignore

def test_parser_images_reference():
    parser = HTMT_Parser(loglevel=LogLevel.NO_LOGS, imagehandling=ImageHandling.REFERENCE)
    assert parser.markdownify(html_img) == markdown_img_reference

def test_parser_images_describe():
    parser = HTMT_Parser(loglevel=LogLevel.NO_LOGS, imagehandling=ImageHandling.DESCRIBE)
    assert parser.markdownify(html_img) == markdown_img_describe

def test_parser_ignores_stuff():
    parser = HTMT_Parser(loglevel=LogLevel.NO_LOGS)
    assert parser.markdownify(html_ignored_stuff) == markdown_ignored_stuff