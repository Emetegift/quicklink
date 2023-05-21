from urllib import request
from urllib.error import HTTPError, URLError


def validate_url(url):
    if not url.startswith('http://') and not url.startswith('https://'):
        url = 'http://' + url
    try:
        request.urlopen(url)
        return True
    except (HTTPError, URLError):
        return False