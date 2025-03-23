import os
import pytest
from bs4 import BeautifulSoup

# Define the path to index.html
INDEX_HTML_PATH = "index.html"

def test_file_exists():
    """Test if index.html file exists."""
    assert os.path.isfile(INDEX_HTML_PATH), "index.html file is missing!"

def test_file_not_empty():
    """Test if index.html is not empty."""
    assert os.path.getsize(INDEX_HTML_PATH) > 0, "index.html file is empty!"

def test_valid_html_structure():
    """Test if index.html contains valid HTML structure."""
    with open(INDEX_HTML_PATH, "r", encoding="utf-8") as file:
        content = file.read()
        soup = BeautifulSoup(content, "html.parser")
    
    assert soup.html is not None, "HTML structure is invalid!"
    assert soup.head is not None, "Missing <head> section!"
    assert soup.body is not None, "Missing <body> section!"

def test_title_present():
    """Test if index.html has a <title> tag."""
    with open(INDEX_HTML_PATH, "r", encoding="utf-8") as file:
        content = file.read()
        soup = BeautifulSoup(content, "html.parser")

    title_tag = soup.find("title")
    assert title_tag is not None, "Missing <title> tag in index.html!"
    assert title_tag.text.strip() != "", "Title tag is empty!"

if __name__ == "__main__":
    pytest.main()

