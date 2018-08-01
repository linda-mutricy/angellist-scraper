__author__ = 'linda-ge'

import re
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

def simple_get(url):
    """
    Attempts to retrieve the content at 'url' by making a HTTP GET request.
    If the response contains HTML/XML, return the text content.
    Otherwise, return None.
    """
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None
    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))

def is_good_response(resp):
    """
    Returns True if the response is HTML. False otherwise.
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200 and content_type is not None and content_type.find('html') > -1)

def log_error(e):
    """Prints the error returned in simple_get."""
    print(e)

def get_list(url):
    response = simple_get(url)

    if response is not None:
        html = BeautifulSoup(response, 'html.parser')
        name_box = html.find('h3', attrs={'class': 's-h3 u-fontSize19 u-fontWeight600'})
        names = set()
        for name in name_box:
            if len(name) > 0:
                names.add(name_box.text.strip())
        return list(names)

    raise Exception('Error retrieving contents at {}'.format(url))

webpage = input('Enter requested URL for scrape: ')
get_list(webpage)
