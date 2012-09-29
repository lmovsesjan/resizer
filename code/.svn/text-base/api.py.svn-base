# encoding: utf-8

from cocaine.context import Log
from cocaine.decorators import simple

from PythonMagick import *

from cocaine.decorators import http

import requests

def factor(width, height, old_width, old_height):
    if 0 == width:
        return float(height) / float(old_height)
    if 0 == height:
        return float(width) / float(old_width)

    f1 = float(old_height) / float(old_width);
    f2 = float(height) / float(width);

    if (f1 < f2):
        return float(height) / float(old_height)
    else:
        return float(width) / float(old_width)

@http
def resize(meta, request):
    url = request['url']

    width = request['width']
    height = request['height']

    r = requests.get(url, timeout = 2)

    img = Image(Blob(r.content))

    f = factor(width, height, img.columns(), img.rows())

    s = "!%sx%s" % (float(img.columns()) * float(f) + 0.5, float(img.rows()) * float(f) + 0.5)

    img.sample(s)

    blob = Blob()
    img.write(blob, "jpg")

    return 200, (('Content-Type', 'image/jpg'), ('Content-Length', str(len(blob.data)))), str(blob.data)
