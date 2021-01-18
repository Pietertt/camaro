import os
from urlparse import urlparse

url = urlparse(request.url).netloc
print(url)
