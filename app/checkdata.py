import re
# as per recommendation from @freylis, compile once only
import xml
import xml.etree.ElementTree
from bs4 import BeautifulSoup

VALID_TAGS = ['img', 'strong', 'em', 'p', 'ul', 'li', 'br', 'h1', "\n"]


def sanitize_html(value):

    soup = BeautifulSoup(value)
    print()
    for tag in soup.findAll(True):
        if tag.name not in VALID_TAGS:
            tag.hidden = True
    print(soup)
    return soup.renderContents()


CLEANR = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')


def cleanhtml(raw_html):
  cleantext = re.sub(CLEANR, '', raw_html)
  return cleantext


def remove_tags(text):
  cleantext = BeautifulSoup(text, "lxml").text
  return cleantext


