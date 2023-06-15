from urllib import request
from urllib.error import HTTPError, URLError


def validate_url(original_url):
    if not original_url.startswith('http://') and not original_url.startswith('https://'):
        original_url = 'https://' + original_url
    try:
        request.urlopen(original_url)
        return True
    except (HTTPError, URLError):
        return False