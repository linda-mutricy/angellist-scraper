__author__ = 'linda-ge'

import csv
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

def get_list(url, filename):
    """
    Creates a simple 2D array of the companies on the given webpage to pass into write_to_csv.
    """
    response = simple_get(url)

    if response is not None:
        html = BeautifulSoup(response, 'html.parser')
        companies = [[h3.find("a").contents[0]] for h3 in html.select("h3[class*='s-h3']")]
        return write_to_csv(companies, filename)

    raise Exception('Error retrieving contents at {}'.format(url))

def write_to_csv(names, filename):
    filename = str(filename)
    with open(str(filename) + ".csv", 'w') as result_file:
        wr = csv.writer(result_file, delimiter = ",")
        wr.writerows(names)

def main():
    webpage = input('Enter requested URL for scrape: ')
    file_name = webpage.rsplit('/', 1)[-1]
    get_list(webpage, file_name)

main()
