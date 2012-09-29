# encoding: utf-8

from cocaine.context import Log
from cocaine.decorators import simple

from PythonMagick import *

from cocaine.decorators import http

import requests

def error(code):
	return code, (), 'Bad request'

def factor(width, height, old_width, old_height):
	if 0 == width:
		return height / old_height
	if 0 == height:
		return width / old_width

	if (old_height / old_width < height / width):
		return height / old_height
	else:
		return width / old_width

@http
def resize(meta, request):
	try:
		url = request['url']

		width = request['width']
		height = request['height']
	except KeyError:
		return error(400)

	try:
		r = requests.get(url, timeout = 2)
	except:
		return error(404)

	img = Image(Blob(r.content))

	args = [float(arg) for arg in (width, height, img.columns(), img.rows())]
	f = factor(*args)

	s = '!%sx%s' % (img.columns() * f + 0.5, img.rows() * f + 0.5)

	img.sample(s)

	blob = Blob()
	img.write(blob, 'jpg')

	return 200, (('Content-Type', 'image/jpg'), ('Content-Length', str(len(blob.data)))), str(blob.data)
